from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render


def register(request):
    if request.user.is_authenticated:
        return redirect('tab1')  # Redirect if already authenticated

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'register.html')

        try:
            user = User.objects.create_user(
                username=email, email=email, password=password)
            user.save()
            auth_login(request, user)
            return redirect('tab1')
        except ValidationError as e:
            messages.error(request, e)

    return render(request, 'register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('tab1')  # Redirect if already authenticated

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('tab1')
        else:
            messages.error(request, 'Wrong credentials')

    return render(request, 'login.html')


@login_required(redirect_field_name='login')
def tab1(request):
    return render(request, 'tab1.html')


def logout(request):
    auth_logout(request)
    return redirect('login')

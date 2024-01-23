from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import UserRegistration


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if UserRegistration.objects.filter(email=email).exists():
            return HttpResponse("This email is already registered.")

        # Create a new user if it doesn't exist
        user = UserRegistration.objects.create(email=email, password=password)
        user.save()

        # Set success in session and Redirect to tab1
        request.session['success'] = True
        return redirect('tab1')

    return render(request, 'register.html')  # Render registration page


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if user exists
        user = authenticate(username=email, password=password)

        if user is not None:
            auth_login(request, user)
            request.session['success'] = True  # Set success in session
            return redirect('tab1')  # Redirect to tab1.html
        else:
            messages.error(request, 'Wrong credentials')

    return render(request, 'login.html')  # Render login page


def tab1(request):
    # Check if user is authenticated and session success is True
    if not request.session.get('success', False):
        return redirect('login')  # Redirect to login page if not authenticated

    # Add your code to render tab1 here
    return render(request, 'tab1.html')


def logout(request):
    auth_logout(request)
    request.session['success'] = False  # Clear success in session
    return redirect('login')

from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .models import UserRegistration


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if UserRegistration.objects.filter(email=email).exists():
            return HttpResponse("This email is already registered.")

        # Create new user
        new_user = UserRegistration(email=email, password=password)
        new_user.save()

        # Redirect to a success page or login page
        return redirect('tab1')

    return render(request, 'register.html')


def success(request):
    # Define your success page view
    return HttpResponse("Registration successful!")

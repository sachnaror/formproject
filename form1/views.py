

from django.shortcuts import redirect, render

from .models import User


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Hash the password using make_password
        # hashed_password = make_password(password)

        # Create and save the user
        # Use the hashed password
        user = User(email=email, password=password)
        user.save()

        return redirect('tab1')  # Redirect to a success page

    return render(request, 'register.html')


def tab1(request):
    return render(request, 'tab1.html')

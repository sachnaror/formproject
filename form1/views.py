
from django.http import HttpResponse
from django.shortcuts import redirect, render


from .models import UserRegistration
from .forms import UserRegistrationForm



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Your registration logic here

            return redirect('tab1')  # Replace 'tab1' with the actual URL name
    else:
        form = UserRegistrationForm()

    return render(request, 'tab1.html', {'form': form})

def success():
    # Define your success page view
    return HttpResponse("Registration successful!")

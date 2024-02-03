

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.forms.models import model_to_dict

from .models import User, tab_one_model

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView


# from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(email=email, password=password)
        user.save()

        return redirect('tab2')  # Redirect to a success page

    return render(request, 'register.html')


def tab1(request):
    return render(request, 'tab1.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User doesn't exist")
            return redirect('login')

        if user.password == password:

            # Save email and cookie in the context
            request.session['email'] = email
            request.session['id'] = user.id
            return redirect('tab1')
        else:
            messages.error(request, "Incorrect password")
            return redirect('login')

    return render(request, 'login.html')


def tab_one(request):
    
    if request.method == 'POST':
        digit = request.POST.get('digit')
        if digit is None:
            raise ValueError("Digit is required")
        digit = int(digit)
        user_id = request.session.get('id')
        user_email = request.session.get('email')
        count = request.session.get('count')
        name = request.POST.get('name')
        country = request.POST.get('country')
        city = request.POST.get('city')
        color = request.POST.get('color')
        ratings = request.POST.get('rating')
        describe = request.POST.get('descrip')
        website = request.POST.get('webs')
        date = request.POST.get('datepik')
        check1 = request.POST.get('box1') == 'on'
        check2 = request.POST.get('box2') == 'on'
        check3 = request.POST.get('box3') == 'on'
        tab_one_instance = tab_one_model(
            digit=digit, user_id=user_id, name=name, country=country, city=city,
            color=color, ratings=ratings, date=date, website=website, describe=describe, check1=check1, check2=check2, check3=check3)
        tab_one_instance.save()
        return redirect('thanks')

    else:
        # Use request.session instead of session
        user_id = request.session.get('id')
        user_email = request.session.get('email')
        count = tab_one_model.objects.filter(user_id=user_id).count()
        count = count+1
        temp = []
        for i in range(1,count):
            temp.append(i)
        context = dict()
        formdata = dict()
        context['formdata'] = formdata
        context['user_id'] = user_id
        context['user_email'] = user_email
        context['count']=count
        context['temp']=temp

        return render(request, 'tab1.html', context)

def edit_tab_one(request):
    if request.method == 'POST':
        print("insdie post")
        digit = request.POST.get('digit')
        if digit is None:
            raise ValueError("Digit is required")
        digit = int(digit)
        user_id = request.session.get('id')
        user_email = request.session.get('email')
        count = request.session.get('count')
        name = request.POST.get('name')
        country = request.POST.get('country')
        city = request.POST.get('city')
        color = request.POST.get('color')
        ratings = request.POST.get('rating')
        describe = request.POST.get('descrip')
        website = request.POST.get('webs')
        date = request.POST.get('datepik')
        check1 = request.POST.get('box1') == 'on'
        check2 = request.POST.get('box2') == 'on'
        check3 = request.POST.get('box3') == 'on'
        tab_one_model.objects.filter(digit=digit).update(digit=digit, user_id=user_id, name=name, country=country, city=city,color=color, ratings=ratings, date=date, website=website, describe=describe, check1=check1, check2=check2, check3=check3)
        return redirect('thanks')
    if(request.method == 'GET'):
        user_id = request.session.get('id')
        user_email = request.session.get('email')
        digit = request.GET.get('digit')
        formdata = tab_one_model.objects.get(digit=digit)
        formdata = model_to_dict(formdata)
        count = tab_one_model.objects.filter(user_id=user_id).count()
        count = count+1
        temp = []
        for i in range(1,count):
            temp.append(i)
        context = dict()
        context['user_id'] = user_id
        context['user_email'] = user_email
        context['count']=digit
        context['temp']=temp
        context['formdata']=formdata
        return render(request, 'tab1.html', context)
def thanks(request):
    print("inside thanks function")
    return render(request, 'thanks.html')


def tab_two(request):
    # Handle POST request
    if request.method == 'POST':
        user_id = request.session.get('id')
        user_email = request.session.get('email')

        context = {
            'user_id': user_id,
            'user_email': user_email
        }

        return render(request, 'tab2.html', context)

    # Handle GET or other request methods
    else:
        # Redirect to a different page
        return HttpResponseRedirect('/thanks/')


def tab2(request):
    return render(request, 'tab2.html')


# class HelloView(APIView):
#     permission_classes = (IsAuthenticated)

#     def get(self):
#         content = {'message': 'Hello, Sachin'}
#         return Response(content)

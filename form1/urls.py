
from django.urls import path
from form1.views import register

urlpatterns = [
    path('register/', register),
]

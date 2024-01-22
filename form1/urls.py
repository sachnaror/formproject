
from django.urls import path
from form1.views import register

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tab1/', views.success, name='tab1'),
    # Other paths...
]

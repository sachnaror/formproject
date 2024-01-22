
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tab1/', views.success, name='tab1'),
    # Other paths...
]

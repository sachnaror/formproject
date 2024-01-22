from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('Tab1/', views.success, name='Tab1'),
    path('login/', views.success, name='login'),
    # Other paths...
]

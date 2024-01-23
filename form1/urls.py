from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('tab1/', views.success, name='tab1'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Other paths...
]

# path('login/', views.login, name='login'),

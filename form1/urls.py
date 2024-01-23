from django.urls import path

from . import views

urlpatterns = [
    path('form1/register/', views.register, name='register'),
    path('form1/login/', views.login, name='login'),
    path('form1/tab1/', views.tab1, name='tab1'),
    # Uncommented and corrected the view function name
    # path('form1/forgotPassword/', views.forgot_password, name='forgotPassword'),
    # path('logout/', views.logout, name='login'),

    # Other paths...
]

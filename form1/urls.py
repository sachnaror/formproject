from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('tab1/', views.tab1, name='tab1'),
    # Uncommented and corrected the view function name
    # path('form1/forgotPassword/', views.forgot_password, name='forgotPassword'),
    # path('logout/', views.logout, name='login'),

    # Other paths...
]

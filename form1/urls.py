from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('tab1/', views.tab1, name='tab1'),
    path('logout/', views.logout, name='logout'),

    # Other paths...
]

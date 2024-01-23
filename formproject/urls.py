
from django.contrib import admin
from django.urls import path
from form1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('tab1/', views.tab1, name='tab1'),
]

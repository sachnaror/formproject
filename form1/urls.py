from django.urls import path

from . import views

urlpatterns = [
    # path('', RedirectView.as_view(url='templates/register.html',
    #                               permanent=True)),
    path('', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tab1/', views.tab1, name='tab1'),
    path('form1/', views.register, name='register'),
    path('form1/register/', views.register, name='register'),

    # Redirect root URL
    # path('form1/', include('form1.urls')),  # Include form1 app's URLs
]

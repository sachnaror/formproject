from django.urls import path

from . import views

urlpatterns = [
    # path('', RedirectView.as_view(url='templates/register.html',
    #                               permanent=True)),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tab1/', views.tab_one, name='tab1'),
    path('thanks/', views.thanks, name='thanks'),
    path('form1/', views.register, name='register'),
    path('form1/register/', views.register, name='register'),
    path('form1/login/', views.login, name='login'),
    path('form1/thanks/', views.thanks, name='thanks'),
    # path('tab_one', views.tab_one, name='tab_one'),
    # path('form1/tab_one', views.tab_one, name='tab_one'),

    # Redirect root URL
    # path('form1/', include('form1.urls')),  # Include form1 app's URLs
]

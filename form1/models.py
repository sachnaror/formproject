from django.db import models
from django.http import HttpResponse


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class tab_one_model(models.Model):
    def your_view(request):
        response = HttpResponse("Your response content")

        # Set the cookie
        response.set_cookie('cookie_name', 'cookie_value')

        return response
    digit = models.IntegerField()
    name = models.TextField()

    def __str__(self):
        return f'{self.digit}'

from django.core.validators import MaxValueValidator
from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class tab_one_model(models.Model):

    digit = models.IntegerField(null=False, validators=[
                                MaxValueValidator(10000000)])
    name = models.TextField(null=False)
    country = models.TextField(null=False)
    CITY_CHOICES = [
        ('Delhi', 'Delhi'),
        ('Gurugram', 'Gurugram'),
        ('Bangalore', 'Bangalore'),
    ]
    city = models.CharField(max_length=100, choices=CITY_CHOICES, null=False)

    def __str__(self):
        return f'{self.digit}'

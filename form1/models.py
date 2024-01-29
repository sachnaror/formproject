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
    # Provide a default value
    name = models.TextField(null=False, default='none')
    country = models.TextField(null=True)

    CITY_CHOICES = [
        ('none', 'None'),  # Adding default value as a choice
        ('Delhi', 'Delhi'),
        ('Gurgaon', 'Gurgaon'),  # cSpell:ignore
        ('Bangalore', 'Bangalore'),  # cSpell:ignore
    ]
    city = models.CharField(
        # Setting default value
        max_length=100, choices=CITY_CHOICES, null=True, default='none')

    rating = models.IntegerField(default=0)

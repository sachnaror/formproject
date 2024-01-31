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
    name = models.TextField(null=False, default='none')
    country = models.TextField(null=True)
    ratings = models.IntegerField(default=0, validators=[MaxValueValidator(5)])
    COLOR_CHOICES = [
        ('none', 'None'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]
    CITY_CHOICES = [
        ('none', 'None'),
        ('Delhi', 'Delhi'),
        ('Gurgaon', 'Gurgaon'),
        ('Bangalore', 'Bangalore'),
    ]
    city = models.CharField(
        max_length=20, choices=CITY_CHOICES, null=True, default='none')
    color = models.CharField(
        max_length=5, choices=COLOR_CHOICES, null=True, default='none')

    # Checkbox fields
    check1 = models.BooleanField(default=False)
    check2 = models.BooleanField(default=False)
    check3 = models.BooleanField(default=False)

    describe = models.CharField(max_length=100, null=False, default='none')

    def __str__(self):
        return f"Digit: {self.digit}, Name: {self.name}, Country: {self.country}, City: {self.city}, Rating: {self.ratings}, Description: {self.describe} Selected color: {self.color}, Check1: {self.check1}, Check2: {self.check2}, Check3: {self.check3}"

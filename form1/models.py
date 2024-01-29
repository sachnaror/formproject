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

    def __str__(self):
        return f"Digit: {self.digit}, Name: {self.name}, Country: {self.country}, City: {self.city}"


class Rating(models.Model):
    ratings = models.IntegerField(default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"Rating: {self.ratings}"


class RadioSelection(models.Model):
    COLOR_CHOICES = [
        ('none', 'None'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    ]
    color = models.CharField(
        max_length=5, choices=COLOR_CHOICES, null=True, default='none')

    def __str__(self):
        return f"Selected color: {self.color}"

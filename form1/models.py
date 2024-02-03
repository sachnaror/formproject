from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models

# from django.utils.translation import gettext as _


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(
        null=False, auto_now_add=True)

    def __str__(self):
        return self.email


def validate_domain_name(value):
    if "://" in value:
        raise ValidationError(
            "Enter only the domain name (without 'http://' or 'https://').")


class tab_one_model(models.Model):
    digit = models.IntegerField(null=False, validators=[
                                MaxValueValidator(10000000)])
    name = models.TextField(null=False, default='none')
    country = models.TextField(null=True)
    ratings = models.IntegerField(default=0, validators=[MaxValueValidator(5)])
    # date = models.DateField(null=True, blank=True)
    date = models.DateField(null=False, auto_now_add=True)
    namesearch = models.CharField(null=False, max_length=100, default='mona')

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

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    tem = models.IntegerField(null=False)

    # (User, on_delete=models.CASCADE, related_name='user_id', default=1)

    domain_name_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$',
        message="Enter a valid domain name (e.g., 'example.com').")

    website = models.CharField(max_length=200, blank=True, validators=[
                               domain_name_validator, validate_domain_name])

    def __str__(self):
        return f"Digit: {self.digit}"

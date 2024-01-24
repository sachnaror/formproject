from django.core.validators import EmailValidator
from django.db import models


class CustomUser(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=128)  # You need to handle hashing

    def __str__(self):
        return self.email

from django.contrib.auth.hashers import make_password
from django.db import models


class UserRegistration(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserRegistration, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

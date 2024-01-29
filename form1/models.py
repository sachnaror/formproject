from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class tab_one_model(models.Model):
    digit = models.IntegerField(null=False)
    name = models.TextField(null=False)
    country = models.TextField(null=True)

    def __str__(self):
        return f'{self.digit}'

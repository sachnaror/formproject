from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class tab_one(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    digit = models.IntegerField()
    name = models.TextField()

    def __str__(self):
        return f'{self.digit}'

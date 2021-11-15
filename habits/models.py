from django.db import models
from django.db.models.expressions import F
from django.contrib.auth.models import User


class Habit(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

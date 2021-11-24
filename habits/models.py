from django.db import models
from django.db.models.expressions import F
from django.contrib.auth.models import User

class Habit(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    interval = models.CharField(max_length=200)
    done = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Habits(models.Model):
    item = models.ForeignKey(
        Habit, on_delete=models.CASCADE)
    next = models.CharField(max_length=200)
    prev = models.CharField(max_length=200)
    count = models.IntegerField()
    def __str__(self):
        return self.item


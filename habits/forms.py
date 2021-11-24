from django import forms
from django.forms import ModelForm
from .models import *


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['url', 'name', "qty", "interval", "done"]

class HabitsForm(forms.ModelForm):
    class Meta:
        model = Habits
        fields = ['item', 'next', "prev", "count"]

from django import forms
from django.forms import ModelForm
from .models import *


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'complete']

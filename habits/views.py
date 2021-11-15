from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from rest_framework import viewsets
from .serializers import HabitSerializer
from .serializers import UserSerializer
from .models import Habit
from .models import User


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all().order_by('user')
    serializer_class = HabitSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    


@login_required
def home(request):
    current_user = request.user

    habits = Habit.objects.filter(user=current_user.id)
    form = HabitForm()
    context = {'habits': habits, 'form': form}
    return render(request, 'habits/list.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def index(request):
    current_user = request.user

    habits = Habit.objects.filter(user=current_user.id)
    form = HabitForm()
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            localForm = form.save(commit=False)
            localForm.user = request.user
            localForm.save()
        return redirect('/')
    context = {'habits': habits, 'form': form}
    return render(request, 'habits/list.html', context)


def updateTask(request, pk):

    habit = Habit.objects.get(id=pk)
    form = HabitForm(instance=habit)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'habits/update_task.html', context)


def deleteTask(request, pk):

    item = Habit.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'habits/delete.html', context)



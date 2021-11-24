from rest_framework import serializers
from .models import Habits, User
from .models import Habit


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habit
        fields = ('url', 'name', "qty", "interval", "done")

class HabitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habits
        fields = ('item', 'next', "prev", "count")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


from .serializer import PomodoroSerializer
from .models import Alarm
from rest_framework import generics

#! ------------------------------  pomodoro --------------- ##
class list_create_pomodoro(generics.ListCreateAPIView):
    queryset = Alarm.objects.all()
    serializer_class = PomodoroSerializer  


class update_delete_retreive_pomodoro(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alarm.objects.all()
    serializer_class =PomodoroSerializer


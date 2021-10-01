
from .serializer import sticknoteSerializer
from .models import StickNote
from rest_framework import generics

#! ------------------------------  pomodoro --------------- ##
class list_create_sticknote(generics.ListCreateAPIView):
    queryset = StickNote.objects.all()
    serializer_class = sticknoteSerializer  


class update_delete_retreive_sticknote(generics.RetrieveUpdateDestroyAPIView):
    queryset = StickNote.objects.all()
    serializer_class =sticknoteSerializer

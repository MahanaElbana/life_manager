
from django.urls import path
from .views import (list_create_pomodoro, update_delete_retreive_pomodoro,)  

app_name='pomodoro'
urlpatterns = [
    path('api/list_create_pomodoro/',list_create_pomodoro.as_view(),name='list_create_pomodoro'),
    path('api/update_delete_retreive_Pomodoro/<int:pk>/',update_delete_retreive_pomodoro.as_view(),name='update_delete_retreive_pomodoro'),

]


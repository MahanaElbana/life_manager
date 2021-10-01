
from django.urls import path
from .views import (list_create_sticknote, update_delete_retreive_sticknote,)  

app_name='sticknote'
urlpatterns = [
    path('api/list_create_sticknote/',list_create_sticknote.as_view(),name='list_create_sticknote'),
    
    path('api/update_delete_retreive_sticknote/<int:pk>/',update_delete_retreive_sticknote.as_view(),name='update_delete_retreive_sticknote'),

]

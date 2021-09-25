from django.urls import path
from .views import (list_create_category, 
                            list_create_media,
                            update_delete_retreive_category, 
                            update_delete_retreive_media,)

app_name='media_manager'
urlpatterns = [
    path('api/list_create_category/',list_create_category,name='list_create_category'),
    path('api/update_delete_retreive_category/<int:id>/',update_delete_retreive_category,name='update_delete_retreive_category'),
    path('api/list_create_media/',list_create_media.as_view(),name='list_create_media'),
    path('api/update_delete_retreive_media/<int:pk>/',update_delete_retreive_media.as_view(),name='update_delete_retreive_media'),

]

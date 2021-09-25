from django.urls import path
from .views import list_create_category,update_delete_retreive_category
app_name='media_manager'
urlpatterns = [
    path('api/list_create_category/',list_create_category,name='list_create_category'),
    path('api/update_delete_retreive_category/<int:id>/',update_delete_retreive_category,name='update_delete_retreive_category')
]

from django.urls import path
from .views import TodoListCreate ,TodoRetrieveUpdateDelete
app_name = 'todo'
urlpatterns = [
    path('api/list_create/',TodoListCreate.as_view(),name="list_create"),
    path('api/retrive_update_delete/<int:pk>/',TodoRetrieveUpdateDelete.as_view(),name="list_create"),
]

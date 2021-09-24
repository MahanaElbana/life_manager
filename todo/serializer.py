
from django.db.models import fields
from rest_framework import serializers 
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    ownerTodo = serializers.CharField(source='ownerTodo.username',read_only=True)
    class Meta:
        model = Todo
        #fields = '__all__'
        fields = ['pk','ownerTodo' ,'title','description' , 'isComplete' ,'taskBegin' ,'taskEnd','grade']


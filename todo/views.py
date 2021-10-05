#from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework import generics
from .permissions import UserOnly
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

# GET -POST - for user and admin 
class TodoList_create(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class =  TodoSerializer
    permission_classes = (UserOnly,)
    authentication_classes = (BasicAuthentication,)


# PUT - DELETE - GET(ID) 
class TodoRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class =  TodoSerializer
    permission_classes = (UserOnly,)
    authentication_classes = (BasicAuthentication,)
    
    # partial updating 
    ##def put(self, request, *args, **kwargs):
    ##    ''' overriding on update method '''
    ##    try:
    ##        todo = Todo.objects.get(pk=kwargs['pk'])
    ##        user = User.objects.get(username=todo.ownerTodo)
    ##    except:
    ##        Response({"item is not exisit or useris not exist"} ,status=status.HTTP_202_ACCEPTED) 
    ##        return
    ##    todoserializer = TodoSerializer(instance=todo ,data=request.data)
    ##    if todoserializer.is_valid():
    ##        todoserializer.save()
    ##        return Response(todoserializer.data ,status=status.HTTP_202_ACCEPTED) 
    ##    return Response("an error ocurs " ,status=status.HTTP_201_CREATED)

    ##! --------------------- OR ----------or-----------##
    def update(self, request, *args, **kwargs):
        ''' overriding on update method '''
        try:
            todo = Todo.objects.get(pk=kwargs['pk'])
            #user = User.objects.get(username=todo.ownerTodo)
        except:
            return Response({"item is not exisit"} ,status=status.HTTP_202_ACCEPTED)
        todoserializer = TodoSerializer(instance=todo ,data=request.data)
        if todoserializer.is_valid():
            todoserializer.save()
            return Response(todoserializer.data ,status=status.HTTP_202_ACCEPTED) 
        return Response("an error ocurs " ,status=status.HTTP_201_CREATED)

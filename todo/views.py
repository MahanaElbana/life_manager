#from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework import generics
from .permissions import UserOnly
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response



# list all user data for admin
class TodoList(generics.ListAPIView):
    queryset =Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    
# retrive one element for admin 
class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

# GET - POST(create) - for user 
class TodoList_create(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class =  TodoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,)
    
    def list(self, request, *args, **kwargs):
        try:
            user = request.user
            todo = Todo.objects.filter(ownerTodo=user)
        except:
            return Response({"item is not exisit"} ,status=status.HTTP_202_ACCEPTED)
        todoserializer = TodoSerializer(todo , many=True)
        return Response(todoserializer.data ,status=status.HTTP_200_OK) 
        
    # def post(self, request, *args, **kwargs):
    #     try:
    #         user = request.user
    #         todo = Todo()
    #         todo.ownerTodo = user 
    #     except:
    #         return Response({"item is not exisit"} ,status=status.HTTP_202_ACCEPTED)
        
    #     todoserializer = TodoSerializer(todo ,data=request.data,)
    #     if todoserializer.is_valid():
    #        todoserializer.save()
    #        return Response(todoserializer.data ,status=status.HTTP_202_ACCEPTED) 
    #     return Response("an error ocurs " ,status=status.HTTP_201_CREATED)


#  PUT - DELETE - GET(ID) (user)
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
    # def update(self, request, *args, **kwargs):
    #     ''' overriding on update method '''
    #     try:
    #         todo = Todo.objects.get(pk=kwargs['pk'])
    #         #user = User.objects.get(username=todo.ownerTodo)
    #     except:
    #         return Response({"item is not exisit"} ,status=status.HTTP_202_ACCEPTED)
    #     todoserializer = TodoSerializer(instance=todo ,data=request.data)
    #     if todoserializer.is_valid():
    #         todoserializer.save()
    #         return Response(todoserializer.data ,status=status.HTTP_202_ACCEPTED) 
    #     return Response("an error ocurs " ,status=status.HTTP_201_CREATED)

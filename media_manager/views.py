from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import serializers, status
# Create your views here.
from .serializer import CategorySerializer,MediaSerializer
from .models import Category,Media

#Category
# LIST & CREATE
@api_view(['GET','POST'])
def list_create_category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)

#UPDATE , DELETE ,RETREIVE
def get_category(id):
    try:
        category = Category.objects.get(pk=id)
        return category
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','PUT','DELETE'])
def update_delete_retreive_category(request,id):
    if request.method == 'GET':
        
        serializer = CategorySerializer(get_category(id))
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = CategorySerializer(get_category(id) , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response('invalid' , status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == 'DELETE':
        
        (get_category(id)).delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    

from django.db.models import fields
from rest_framework import serializers
from .models import Category,Media
class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    #medias = MediaSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'
        
    

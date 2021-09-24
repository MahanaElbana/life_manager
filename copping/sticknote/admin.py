from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import StickNote
# Register your models here.
admin.site,register(StickNote)
from django.db import models

# Create your models here.
class StickNote(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    
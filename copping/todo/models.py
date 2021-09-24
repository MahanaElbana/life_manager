from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now=True)
    isComplete = models.BooleanField(default = False)
    taskBegin = models.DateTimeField()
    taskEnd = models.DateTimeField()
    grade = models.FloatField(default = 0.0)
    
    def __str__(self):
        return self.title
    
    
from django.db import models

# Create your models here.
mediaType = [
        ('file', 'file'),
        ('text', 'text'),
        ('url', 'url'),
    ]
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length= 300 )
    
    def __str__(self):
        return self.name
    
class Media(models.Model):
    #media_type = models.CharField(max_length=50, choices=mediaType ,default='file')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    file = models.FileField(upload_to='media/' , null = True , blank = True)
    url = models.URLField(max_length=200 , null = True, blank=True)
    text = models.TextField(max_length=300, null=True )
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)
    dateAdded = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return self.title
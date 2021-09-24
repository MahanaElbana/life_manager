from django.db import models
sessionMenue=[
    (25,'25 min'),
    (30,'30 min'),
    (45,'45 min'),
]
breakTime=[
    (5,'short break'),
    (15,'long break'),
]
# Create your models here.
class Alarm(models.Model):
    name = models.CharField(max_length=50)
    sessitionTime=models.IntegerField(choices=sessionMenue, default=25)
    breakTime=models.IntegerField(choices=breakTime, default = 5)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
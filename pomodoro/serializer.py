
from rest_framework.serializers import ModelSerializer
from .models import Alarm
class PomodoroSerializer(ModelSerializer):
    
    class Meta:
        model = Alarm
        fields = ['pk','name','sessitionTime','breakTime','created_at']



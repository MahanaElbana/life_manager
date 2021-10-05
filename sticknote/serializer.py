
from rest_framework.serializers import ModelSerializer
from .models import StickNote
class StickNoteSerializer(ModelSerializer):
    
    class Meta:
        model = StickNote
        fields = "__all__"


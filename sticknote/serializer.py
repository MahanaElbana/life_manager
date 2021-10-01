
from rest_framework.serializers import ModelSerializer
from .models import StickNote
class sticknoteSerializer(ModelSerializer):
    
    class Meta:
        model = StickNote
        fields = "__all__"


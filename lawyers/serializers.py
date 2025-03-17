from rest_framework import serializers
from .models import LawyerProfile

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawyerProfile
        fields = "__all__"

from rest_framework import serializers
from .models import comments

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = '__all__'
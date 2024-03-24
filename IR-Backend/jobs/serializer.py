from rest_framework import serializers
from .models import jobs

class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobs
        fields = '__all__'
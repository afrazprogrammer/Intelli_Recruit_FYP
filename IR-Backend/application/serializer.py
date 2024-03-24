from rest_framework import serializers
from .models import saved_jobs, analytics

class savedjobSerializer(serializers.ModelSerializer):
    class Meta:
        model = saved_jobs
        fields = '__all__'


class jobanalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = analytics
        fields = '__all__'
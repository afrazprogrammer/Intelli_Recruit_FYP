from rest_framework import serializers
from .models import int_evaluation, jobinterview

class evaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = int_evaluation
        fields = '__all__'


class interviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobinterview
        fields = '__all__'
from rest_framework import serializers
from .models import Company, JobSeeker, CompanyLocation, CompanyProjects, Skill, Project

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class jobseekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class complocSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLocation
        fields = '__all__'

class comprojSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProjects
        fields = '__all__'

class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class projSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'









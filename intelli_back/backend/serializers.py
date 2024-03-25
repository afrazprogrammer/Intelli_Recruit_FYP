from rest_framework.serializers import ModelSerializer
from .models import Company, JobSeeker, Education, WorkExp, Jobs, JobsSaved, Interviews, Feedback

class companySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class jobseekerSerializer(ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class educationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class workexpSerializer(ModelSerializer):
    class Meta:
        model = WorkExp
        fields = '__all__'

class jobsSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class jobssavedSerializer(ModelSerializer):
    class Meta:
        model = JobsSaved
        fields = '__all__'

class interviewsSerializer(ModelSerializer):
    class Meta:
        model = Interviews
        fields = '__all__'

class feedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
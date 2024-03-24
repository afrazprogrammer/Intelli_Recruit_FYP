from django.db import models
from django.utils.timezone import now

# Create your models here.
class jobinterview(models.Model):
    applicant_email = models.EmailField()
    applicant_first_name = models.CharField(max_length=255)
    applicant_last_name = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()
    date = models.DateField(default=now)
    job_title = models.CharField(max_length=255)
    company_email = models.EmailField()
    job_posted_date = models.DateField()

    def __str__(self):
        return f"{self.applicant_email} - {self.job_title} Interview"
    
class int_evaluation(models.Model):
    applicant_email = models.EmailField()
    job_title = models.CharField(max_length=255)
    company_email = models.EmailField()
    interview_date = models.DateField()
    personality_test_result = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    job_posted_date = models.DateField()

    def __str__(self):
        return f"{self.user_email} - {self.job_title} Interview Evaluation"

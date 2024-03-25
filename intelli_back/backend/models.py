from django.db import models
from PIL import Image

# Create your models here.
def upload_to(file, filename):
    pass

class Company(models.Model):
    company_name = models.CharField(max_length = 100, null = True, blank = True)
    username = models.CharField(max_length = 100, null = True, blank = True)
    company_password = models.CharField(max_length = 100, null = True, blank = True)
    company_email = models.CharField(max_length = 100, null = True, blank = True)
    company_location = models.CharField(max_length = 100, null = True, blank = True)
    company_address = models.TextField(null = True, blank = True)
    company_dob = models.CharField(max_length = 100, null = True, blank = True)
    company_au = models.TextField(null = True, blank = True)
    company_mission = models.TextField(null = True, blank = True)
    company_services = models.TextField(null = True, blank = True)
    company_logo = models.ImageField(upload_to='backend/images', default = 'backend/images/default.png', null = True, blank = True)

    def __str__(self):
        return self.company_name
    
class JobSeeker(models.Model):
    applicant_name = models.CharField(max_length = 100, null = True, blank = True)
    username = models.CharField(max_length = 100, null = True, blank = True)
    applicant_password = models.CharField(max_length = 100, null = True, blank = True)
    applicant_email = models.CharField(max_length = 100, null = True, blank = True)
    applicant_location = models.CharField(max_length = 100, null = True, blank = True)
    applicant_address = models.TextField(null = True, blank = True)
    applicant_dob = models.CharField(max_length = 100, null = True, blank = True)
    applicant_profession = models.CharField(max_length = 100, null = True, blank = True)
    applicant_education = models.CharField(max_length = 100, null = True, blank = True)
    applicant_skills = models.TextField(null = True, blank = True)
    applicant_workexp = models.CharField(max_length = 100, null = True, blank = True)
    applicant_pfp = models.ImageField(upload_to='backend/images', default = 'backend/images/default.png', null = True, blank = True)

    def __str__(self):
        return self.applicant_name
    
class Education(models.Model):
    degree = models.CharField(max_length = 100, null = True, blank = True)
    institute = models.CharField(max_length = 300, null = True, blank = True)
    grad_year = models.CharField(max_length = 100, null = True, blank = True)
    cgpa = models.CharField(max_length = 10, null = True, blank = True)
    f_key = models.CharField(max_length = 100, null = True, blank = True)
    
    def __str__(self):
        return self.institute
    
class WorkExp(models.Model):
    title = models.CharField(max_length = 100, null = True, blank = True)
    company_name = models.CharField(max_length = 100, null = True, blank = True)
    start = models.CharField(max_length = 100, null = True, blank = True)
    end = models.CharField(max_length = 100, null = True, blank = True)
    desc = models.TextField(null = True, blank = True)
    f_key = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.title
    
class Jobs(models.Model):
    title = models.CharField(max_length = 100, null = True, blank = True)
    company_email = models.CharField(max_length = 100, null = True, blank = True)
    department = models.CharField(max_length = 100, null = True, blank = True)
    location = models.CharField(max_length = 100, null = True, blank = True)
    job_type = models.CharField(max_length = 100, null = True, blank = True)
    req_exp = models.CharField(max_length = 100, null = True, blank = True)
    salary = models.CharField(max_length = 100, null = True, blank = True)
    job_description = models.TextField(null = True, blank = True)
    key_responsibilities = models.TextField(null = True, blank = True)
    required_skills = models.TextField(null = True, blank = True)
    views = models.CharField(null = True, blank = True, max_length = 100)
    applied = models.CharField(null = True, blank = True, max_length = 100)
    saved = models.CharField(null = True, blank = True, max_length = 100)
    
    def __str__(self):
        return self.title
    
class JobsSaved(models.Model):
    title = models.CharField(max_length = 100, null = True, blank = True)
    company_email = models.CharField(max_length = 100, null = True, blank = True)
    applicant_email = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.title
    
class Interviews(models.Model):
    title = models.CharField(max_length = 100, null = True, blank = True)
    company_email = models.CharField(max_length = 100, null = True, blank = True)
    applicant_email = models.CharField(max_length = 100, null = True, blank = True)
    questions = models.TextField(null = True, blank = True)
    answers = models.TextField(null = True, blank = True)
    e_result = models.CharField(max_length = 100, null = True, blank = True)
    t_result = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    user = models.CharField(max_length = 100, null = True, blank = True)
    rating = models.CharField(max_length = 1, null = True, blank = True)
    feedback = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.feedback
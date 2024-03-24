from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    contact_no = models.CharField(max_length=20)
    about = models.TextField()
    min_salary_offered = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    company_picture = models.ImageField(upload_to='company_pictures/', null=True, blank=True)
    instagram_account = models.URLField(null=True, blank=True)
    facebook_account = models.URLField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'ircompany'
        app_label = 'Profile'


    def __str__(self):
        return self.name

class JobSeeker(models.Model):
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    about_you = models.TextField()
    education = models.TextField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    profile_link = models.URLField(null=True, blank=True)
    experience_years = models.DecimalField(max_digits=4, decimal_places=2)
    awards = models.TextField(null=True, blank=True)
    certificates = models.TextField(null=True, blank=True)

    class Meta:
       db_table = 'jobseeker'
       app_label = 'Profile'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CompanyLocation(models.Model):
    #company name
    email = models.EmailField(max_length=255,default=None)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    class Meta:
        db_table = 'companylocations'
        app_label = 'Profile'


    def __str__(self):
        return self.name

class CompanyProjects(models.Model):
    # company name
    email = models.EmailField(max_length=255,default=None)
    project_name = models.CharField(max_length=200)
    project_duration = models.CharField(max_length=100)
    client_name = models.CharField(max_length=200)
    project_description = models.TextField()

    class Meta:
        db_table = 'companyprojects'
        app_label = 'Profile'


    def __str__(self):
        return self.project_name

## job seeker projects
class Project(models.Model):
    # job seeker name
    email = models.EmailField(max_length=255,default=None)
    #job seeker cnic
    company = models.CharField(max_length=15)
    project_name = models.CharField(max_length=200)
    project_duration = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = 'jobseekerprojects'
        app_label = 'Profile'

    def __str__(self):
        return self.project_name

# job seeker skills
class Skill(models.Model):
    # job seeker name
    email = models.EmailField(max_length=255, default=None)
    #job seeker cnic which is unique
    cnic = models.CharField(max_length=15)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'skillss'
        app_label = 'Profile'

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
# user can save a job to view and apply for it later
class saved_jobs(models.Model):
    user_email = models.EmailField()
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=255)
    date_posted = models.DateField()

    def __str__(self):
        return f'{self.user_email} - {self.job_title}'

# to show the popularity of the job by displaying no of views etc.
class analytics(models.Model):
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=255)
    date_posted = models.DateField()
    views = models.PositiveIntegerField(default=0)
    saved = models.PositiveIntegerField(default=0)
    applied = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.company_email} - {self.job_title}'
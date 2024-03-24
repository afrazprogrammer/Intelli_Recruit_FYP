from django.db import models
from django.utils.timezone import now

# Create your models here.
class jobs(models.Model):
    company_email = models.EmailField(max_length=255)
    company_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255) 
    job_description = models.TextField()
    posted_date = models.DateField(default=now)
    salary_package = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.TextField()
    required_skills = models.TextField()
    post = models.CharField(max_length=2551)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    experience_required_years = models.DecimalField(max_digits=4, decimal_places=2)
    education_required = models.TextField()
    loc = models.CharField(max_length=50, default=None, null=True) # remote or on site job
    # Field to indicate the status of the job (e.g., hiring, filled)
    job_status = models.CharField(
        max_length=20,
        choices=[
            ('hiring', 'Hiring'),
            ('filled', 'Filled'),
        ],
        default='hiring',
    )

    class Meta:
        # Define unique together constraint for title and company_name
        unique_together = ('title', 'company_email','posted_date')

    def __str__(self):
        return self.title
from .models import jobs

def delete_jobs_listing_data(company_email):
    if jobs.objects.filter(company=company_email).exists():
        jobs.objects.filter(company=company_email).delete()
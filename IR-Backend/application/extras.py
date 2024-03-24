from .models import saved_jobs, analytics

def delete_savedjobs_listing_data(company_email):
    if saved_jobs.objects.filter(company=company_email).exists():
        saved_jobs.objects.filter(company=company_email).delete()


def delete_statistics_listing_data(company_email):
    if analytics.objects.filter(company=company_email).exists():
        analytics.objects.filter(company=company_email).delete()


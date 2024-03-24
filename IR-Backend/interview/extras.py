from .models import jobinterview, int_evaluation

def delete_interview_listing_data(company_email):
    if jobinterview.objects.filter(company_email=company_email).exists():
       jobinterview.objects.filter(company_email=company_email).delete()


def delete_evaluation_listing_data(company_email):
    if int_evaluation.objects.filter(company_email=company_email).exists():
        int_evaluation.objects.filter(company_email=company_email).delete()
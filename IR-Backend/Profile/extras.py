from .models import Company, CompanyLocation, CompanyProjects, JobSeeker, Skill, Project

def delete_company_listing_data(company_email):
    if Company.objects.filter(email=company_email).exists():
       Company.objects.filter(email=company_email).delete()


def delete_applicant_listing_data(user_email):
    if JobSeeker.objects.filter(email=user_email).exists():
        JobSeeker.objects.filter(email=user_email).delete()

def delete_loc_listing_data(company_email):
    if CompanyLocation.objects.filter(email=company_email).exists():
        CompanyLocation.objects.filter(email=company_email).delete()

def delete_comproj_listing_data(company_email):
    if CompanyProjects.objects.filter(email=company_email).exists():
        CompanyProjects.objects.filter(email=company_email).delete()

def delete_skill_listing_data(user_email):
    if Skill.objects.filter(email=user_email).exists():
        Skill.objects.filter(email=user_email).delete()

def delete_proj_listing_data(user_email):
    if Project.objects.filter(email=user_email).exists():
       Project.objects.filter(email=user_email).delete()
from django.urls import path
from .views import interviewApplicantView, interviewCompanyView, evaluationView

urlpatterns = [
    path('applicant',  interviewApplicantView.as_view()),
    path('company', interviewCompanyView.as_view()),
    path('evaluation', evaluationView.as_view())
]

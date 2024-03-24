from django.urls import path
from .views import compView, complocView, comprojView, jobseekerView, skillView, projView

urlpatterns = [
    path('company/profile',  compView.as_view()),
    path('company/location', complocView.as_view()),
    path('company/project', comprojView.as_view()),
    path('applicant/profile', jobseekerView.as_view()),
    path('applicant/skill', skillView.as_view()),
    path('applicant/project', projView.as_view()),
]
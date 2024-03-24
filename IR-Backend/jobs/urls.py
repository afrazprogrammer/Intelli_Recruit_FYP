from django.urls import path
from .views import ManagejobView, joblistView, searchjobView, savedjoblistView

urlpatterns = [
    path('manage',  ManagejobView.as_view()),
    path('detail', joblistView.as_view()),
    path('search', searchjobView.as_view()),
    path('saved_job', savedjoblistView.as_view()),
]
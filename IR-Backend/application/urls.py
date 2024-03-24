from django.urls import path
from .views import ManagesavedjobView, ManagestatisticsView

urlpatterns = [
    path('savedjobs',  ManagesavedjobView.as_view()),
    path('jobs_statistics', ManagestatisticsView.as_view()),
]

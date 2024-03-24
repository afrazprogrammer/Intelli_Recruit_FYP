from django.urls import path
from .views import commentView

urlpatterns = [
    path('comments',  commentView.as_view()),
]

# to create urls end points

from django.urls import path
from .views import RegisterView, RetrieveUserView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user_data', RetrieveUserView.as_view())
]
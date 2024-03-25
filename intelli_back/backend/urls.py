from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('api', views.index, name='index'),
    path('api/registeruser', views.register_user, name = "register"),
    path('api/gettype', views.get_type, name = "gettype"),
    path('api/r/getjoblist', views.getjoblist_company, name = "company jobs"),
    path('api/r/getjob', views.getjob_company, name = "company job"),
    path('api/r/getcompany', views.get_company, name = "getcompany"),
    path('api/c/getjoblist', views.getjobs_applicant, name = "getjobs_applicant"),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
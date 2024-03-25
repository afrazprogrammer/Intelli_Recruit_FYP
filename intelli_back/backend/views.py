from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import companySerializer, jobseekerSerializer, educationSerializer, workexpSerializer, jobsSerializer, jobssavedSerializer, interviewsSerializer, feedbackSerializer 
from .models import Company, JobSeeker, Education, WorkExp, Jobs, JobsSaved, Interviews, Feedback
from django.contrib.auth.models import User
#from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


#model = SentenceTransformer('all-MiniLM-L6-v2')
'''def sim(user_profile, job_descriptions):
    user_vector = model.encode(user_profile)
    job_vectors = model.encode(job_descriptions[:][1])

    similarities = cosine_similarity([user_vector], job_vectors)

    top_n_indices = np.argsort(similarities[0])
    recommended_jobs = [job_descriptions[i] for i in top_n_indices]

    print("Recommended Jobs:", recommended_jobs)'''


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)

@api_view(['POST'])
def register_user(request):
    if request.method == "POST":
        data = request.data

        user_type = data['type']

        if user_type == "recruiter":
            company = Company.objects.create(
                username = data['username'],
                company_password = data['password'],
                company_email = data['email']
            )

            user = User.objects.create_user(
                username = data['username'],
                password = data['password'],
                email = data['email']
            )

            serializer = companySerializer(company)

            user.save()

            return Response(serializer.data)
        else:
            jobseeker = JobSeeker.objects.create(
                username = data['username'],
                applicant_password = data['password'],
                applicant_email = data['email']
            )

            user = User.objects.create_user(
                username = data['username'],
                password = data['password'],
                email = data['email']
            )

            serializer = jobseekerSerializer(jobseeker)

            user.save()

            return Response(serializer.data)
        
@api_view(['POST'])
def get_type(request):
    if request.method == 'POST':
        data = request.data

        company = Company.objects.filter(company_email = data['email'])
        jobseeker = JobSeeker.objects.filter(applicant_email = data['email'])

        if company:
            return Response("Company!")
        elif jobseeker:
            return Response("JobSeeker!")
        
@api_view(['POST'])
def getjoblist_company(request):
    if request.method == 'POST':
        data = request.data

        job = Jobs.objects.filter(company_email = data['email'])

        print(job)
        serializer = jobsSerializer(job, many = True)

        return Response(serializer.data)
    
@api_view(['POST'])
def getjob_company(request):
    if request.method == 'POST':
        data = request.data

        job = Jobs.objects.filter(company_email = data['email'], title = data['title'])

        print(data)

        serializer = jobsSerializer(job, many = True)

        return Response(serializer.data)
    
@api_view(['POST'])
def get_company(request):
    if request.method == 'POST':
        data = request.data
        print("Data: ", request.data)
        company = Company.objects.filter(company_email = data['email']).values()

        print(company[0])

        serializer = companySerializer(company, many = True)

        return Response(company[0])
    
@api_view(['POST'])
def getjobs_applicant(request):
    if request.method == "POST":
        data = request.data

        print("Data: ", data)

        applicant = JobSeeker.objects.filter(applicant_email = data['email']).values()

        applicant_skills = "#".split(applicant[0]['applicant_skills'])

        jobs = Jobs.objects.all().values()

        jobs_ = [(i["title"], i['required_skills']) for i in jobs]
        print(jobs_)

        #recommender.sim(applicant_skills, jobs_)

        return Response(applicant[0])
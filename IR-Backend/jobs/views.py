from django.shortcuts import render
from rest_framework.views import APIView
from .models import jobs
from rest_framework import status, permissions
from rest_framework.response import Response
import datetime
from .serializer import jobSerializer
from django.contrib.postgres.search import SearchVector, SearchQuery
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db.models import Q


# Create your views here.

# company views, fetch job listing containing all the jobs posted by it
# create a new job
class ManagejobView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            if user.is_company:
                # Company user can view all jobs posted by itself
                job_list = jobs.objects.order_by('-posted_date').filter(company_email=user.email)
            else:
                return Response({'error': 'User does not have necessary permissions for getting this job listing data'},
                                status=status.HTTP_403_FORBIDDEN)

            job_list = jobSerializer(job_list, many=True)
            return Response({'listss': job_list.data}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving the job list'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self,data):
        company_name = data['company_name']
        company_email = data['company_email']
        company_email = company_email.lower()
        title = data['title']
        job_description = data['job_description']
        posted_date = data.get('posted_date', datetime.date.today())  # If not provided, use today's date
        salary_package = data['salary_package']
        benefits = data['benefits']
        required_skills = data['required_skills']
        post = data['post']
        city = data['city']
        country = data['country']
        experience_required_years = data['experience_required_years']
        education_required = data['education_required']
        loc = data['loc']
        job_status = data.get('job_status', 'hiring')  # If not provided, default to 'hiring'
        
        data = {
            'company_name': company_name,
            'company_email': company_email,
            'title': title,
            'job_description': job_description,
            'posted_date': posted_date,
            'salary_package': salary_package,
            'benefits': benefits,
            'required_skills': required_skills,
            'post': post,
            'city': city,
            'country': country,
            'experience_required_years': experience_required_years,
            'education_required': education_required,
            'loc': loc,
            'job_status': job_status,
}
        return data

    
    def post(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User does not have permission to create a job'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            # Add the new fields to the data dictionary
            company_name = data['company_name']
            company_email = data['company_email']
            company_email = company_email.lower()
            title = data['title']
            job_description = data['job_description']
            posted_date = data.get('posted_date', datetime.date.today())  # If not provided, use today's date
            salary_package = data['salary_package']
            benefits = data['benefits']
            required_skills = data['required_skills']
            post = data['post']
            city = data['city']
            country = data['country']
            experience_required_years = data['experience_required_years']
            education_required = data['education_required']
            loc = data['loc']
            job_status = data.get('job_status', 'hiring')  # If not provided, default to 'hiring'

            # Check if required fields are present
            required_fields = ['company_name', 'company_email', 'title', 'job_description', 'salary_package', 'loc','benefits', 'required_skills', 'post', 'city', 'country', 'experience_required_years', 
                               'education_required']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if job with the same title and company name already exists
            if jobs.objects.filter(title=title, company_name=company_name, company_email=company_email, posted_date=posted_date).exists():
                return Response({'error': 'Job with the same title and company name already exists'}, 
                                status=status.HTTP_400_BAD_REQUEST)
            
            # Create job
            job = jobs.objects.create(
                company_name=company_name,
                company_email=company_email,
                title=title,
                job_description=job_description,
                posted_date=posted_date,
                salary_package=salary_package,
                benefits=benefits,
                required_skills=required_skills,
                post=post,
                city=city,
                country=country,
                experience_required_years=experience_required_years,
                education_required=education_required,
                job_status=job_status,
                loc = loc
            )

            return Response({'success': 'Job created Successfully', 'job_id': job.id}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating a job: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User does not have permission to update job details'}, 
                                status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)

            # Extract title and posted date from request data
            title = data.pop('title', None)
            posted_date = data.pop('posted_date', None)
            
            if title is None or posted_date is None:
                return Response({'error': 'Title and posted date are required for updating job details'}, 
                                status=status.HTTP_400_BAD_REQUEST)

            # Update job details
            jobs.objects.filter(title=title, posted_date=posted_date, company_email=user.email).update(**data)

            return Response({'success': 'Job details updated successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating the job: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            

    # to update a piece or data, to update the status of the job whether the company is hiring or is filled
    def patch(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User does not have permission to update a job details'}, 
                                status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            job_status = data.get('job_status')
            title = data.get('title')
            posted_date = data.get('posted_date')
            if title is None or posted_date is None or job_status is None:
                return Response({'error': 'Title and posted date are required for updating job details'}, 
                                status=status.HTTP_400_BAD_REQUEST)

            
            # Check if the job exists and belongs to the company user
            job = jobs.objects.filter(title=title,posted_date=posted_date, company_email=user.email).first()
            if not job:
                return Response({'error': 'Job not found or does not belong to the company user'}, 
                                status=status.HTTP_404_NOT_FOUND)
            # Update the job status
            job.job_status = job_status
            job.save()

            return Response({'success': 'Job status updated successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating the job status : {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    # deleting a job
    def delete(self,request):
        try:
          user = request.user
          if not user.is_company:
                return Response({'error': 'User does not have permission to delete a job'}, 
                                status=status.HTTP_403_FORBIDDEN)
          
          data = request.data
          job_title = data['title']
          posted_date = data['posted_date']
          if not jobs.objects.filter(company_email=user.email, title=job_title, posted_date = posted_date).exists():
              return Response(
                  {'error':'Job that you are trying to delete does not exists'},
                  status=status.HTTP_404_NOT_FOUND
              )
          jobs.objects.filter(company_email=user.email, title=job_title).delete()

          if not jobs.objects.filter(company_email=user.email, title=job_title).exists():
              return Response(
                  status=status.HTTP_204_NO_CONTENT
              )
          
          else:
              return Response(
                  {'error':"Failed to delete a job"},
                  status = status.HTTP_400_BAD_REQUEST
              )

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting a job : {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# job seeker view
# get all the job listings
class joblistView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            
            if not user.is_company:
                # Non-company users (job seekers) can view all posted jobs with latest jobs first
                job_list = jobs.objects.order_by('-posted_date')
                job_list = jobSerializer(job_list, many=True)
                return Response({'job_list': job_list.data}, status=status.HTTP_200_OK)
            else:
                # For company users, return an empty list
                return Response({'job_list': []}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving the job list'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#display job details by job posted date, job name and company email 
class savedjoblistView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            
            if not user.is_company:
                # Get parameters from the request query
                posted_date = request.query_params.get('posted_date')
                job_name = request.query_params.get('title')
                company_email = request.query_params.get('company_email')

                # Filter job listings based on the provided parameters
                job_list = jobs.objects.filter(posted_date=posted_date, title=job_name, company_email=company_email)
                
                # Serialize the job list
                job_list = jobSerializer(job_list, many=True)
                
                # Return the serialized job list as a response
                return Response({'job_list': job_list.data}, status=status.HTTP_200_OK)
            else:
                # For company users, return an empty list
                return Response({'job_list': []}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving the job list'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# search a job by keyword
class searchjobView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        try:
            # Check if the user is not a company user
            if request.user.is_company:
                return Response(
                    {'error': 'Company users are not allowed to search for jobs'},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Get the search keyword from query parameters
            search_fields = ['country', 'post', 'company_name', 'loc', 'salary_package']
            search_keyword = None
            for field in search_fields:
                if field in request.query_params:
                    search_keyword = request.query_params.get(field)
                    if field == 'salary_package':
                        try:
                            search_keyword = Decimal(search_keyword)
                        except ValueError:
                            return Response(
                                {'error': 'salary_package must be a decimal number'},
                                status=status.HTTP_400_BAD_REQUEST
                            )
                    break

            if not search_keyword:
                return Response(
                    {'error': 'Must pass a valid search keyword'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Create a query for filtering jobs based on search criteria
            query = Q(**{field + '__icontains': search_keyword})
            if field == 'job_status':
                query &= Q(**{field: search_keyword.lower()})

            # Filter jobs based on query
            listing = jobs.objects.filter(query)

            if not listing.exists():
                return Response(
                    {'error': 'No listings found with this criteria'},
                    status=status.HTTP_404_NOT_FOUND
                )

            listing = jobSerializer(listing, many=True)
            return Response(
                {'listings': listing.data},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({'error': f'Something went wrong while searching a job : {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

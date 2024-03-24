from django.shortcuts import render
from rest_framework.views import APIView
from .models import saved_jobs, analytics
from rest_framework import status, permissions
from rest_framework.response import Response
import datetime
from .serializer import savedjobSerializer, jobanalyticsSerializer
from rest_framework.permissions import IsAuthenticated

# saved jobs views
class ManagesavedjobView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            if not user.is_company:
                # Company user can view all jobs posted by itself
                job_list = saved_jobs.objects.order_by('-date_posted').filter(user_email=user.email)
            else:
                return Response({'error': 'User does not have necessary permissions for getting this job listing data'},
                                status=status.HTTP_403_FORBIDDEN)

            job_list = savedjobSerializer(job_list, many=True)
            return Response({'listss': job_list.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong while retrieving the saved job list: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self,data):
        company_name = data['company_name']
        company_email = data['company_email']
        user_email = data['user_email']
        company_email = company_email.lower()
        job_title = data['job_title']
        date_posted = data['date_posted'] 
        
        data = {
            'company_name': company_name,
            'company_email': company_email,
            'user_email':user_email,
            'job_title': job_title,
            'date_posted': date_posted,
}
        return data

    
    def post(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User does not have permission to save a job'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            # Add the new fields to the data dictionary
            company_name = data['company_name']
            company_email = data['company_email']
            data['user_email'] = user.email
            user_email = data['user_email']
            user_email = user_email.lower()
            company_email = company_email.lower()
            job_title = data['job_title']
            date_posted = data['date_posted'] 
            # Check if required fields are present
            required_fields = ['company_name', 'company_email', 'job_title', 'user_email','date_posted']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if job with the same title and company name already exists
            if saved_jobs.objects.filter(job_title=job_title, company_name=company_name, company_email=company_email).exists():
                return Response({'error': 'Job with the same title and company name already exists in the job saved list'}, 
                                status=status.HTTP_400_BAD_REQUEST)
            
            # Create job
            job = saved_jobs.objects.create(
                company_name=company_name,
                company_email=company_email,
                user_email = user_email,
                job_title=job_title,
                date_posted=date_posted
            )

            return Response({'success': 'Job saved Successfully', 'job_id': job.id}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when saving a job: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    
    # deleting a job by its id
    def delete(self,request):
        try:
          user = request.user
          if user.is_company:
                return Response({'error': 'User does not have permission to delete a saved job'}, 
                                status=status.HTTP_403_FORBIDDEN)
          
          data = request.data
          job_id = data['id']
          if not saved_jobs.objects.filter(user_email=user.email, id=job_id).exists():
              return Response(
                  {'error':'Job that you are trying to delete does not exists'},
                  status=status.HTTP_404_NOT_FOUND
              )
          saved_jobs.objects.filter(user_email=user.email, id=job_id).delete()

          if not saved_jobs.objects.filter(user_email=user.email, id=job_id).exists():
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
        


# job statistics views
class ManagestatisticsView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            # Get parameters from request
            job_title = request.query_params.get('job_title')
            company_name = request.query_params.get('company_name')
            date_posted = request.query_params.get('date_posted')

            if user.is_company:
                # Company user can view job statistics based on job title, company name, and posted date
                job_list = analytics.objects.filter(job_title=job_title, company_name=company_name, date_posted=date_posted, company_email=user.email)
            else:
                # Non-company users can view job statistics based on job title, company name, and posted date
                job_list = analytics.objects.filter(job_title=job_title, company_name=company_name, date_posted=date_posted)
            
            # Serialize the queryset
            serializer = jobanalyticsSerializer(job_list, many=True)

            return Response({'Job Statistics': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong while retrieving job statistics: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self,data):
        company_name = data['company_name']
        company_email = data['company_email']
        company_email = company_email.lower()
        job_title = data['job_title']
        date_posted = data['date_posted']
        views = data['views']
        saved = data['saved']
        applied = data['applied']
            
        data = {
            'company_name': company_name,
            'company_email': company_email,
            'job_title': job_title,
            'date_posted': date_posted,
            'views': views,
            'saved': saved,
            'applied':applied
}
        return data

    
    def post(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User does not have permission to access this functionality'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            # Add the new fields to the data dictionary
            company_name = data['company_name']
            company_email = data['company_email']
            company_email = company_email.lower()
            job_title = data['job_title']
            date_posted = data['date_posted']
            views = data['views']
            saved = data['saved']
            applied = data['applied']
            # Check if required fields are present
            required_fields = ['company_name', 'company_email', 'job_title', 'date_posted','views','saved','applied']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if job with the same title and company name already exists
            if analytics.objects.filter(job_title=job_title, company_name=company_name, company_email=company_email, date_posted=date_posted,
                                   views=views, saved=saved, applied=applied).exists():
                return Response({'error': 'Job with the same title and company name already exists'}, 
                                status=status.HTTP_400_BAD_REQUEST)
            
            # Create job
            job = analytics.objects.create(
                company_name=company_name,
                company_email=company_email,
                job_title = job_title,
                date_posted = date_posted,
                views = views,
                saved = saved,
                applied=applied

            )

            return Response({'success': 'Job Statistics created Successfully', 'job_id': job.id}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating a job: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    def patch(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User does not have permission to update job statistics details'}, 
                                status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            job_title = data['job_title']
            company_name = data['company_name']
            date_posted = data['date_posted']
            update_field = data.get('update_field')  # Field to update (views, applied, saved)
            update_value = data.get('update_value')  # New value for the field

            if not job_title or not company_name or not date_posted or not update_field or update_field not in ['views', 'applied', 'saved']:
                return Response({'error': 'Invalid input data'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the job exists
            job = analytics.objects.filter(job_title=job_title,company_name=company_name, date_posted=date_posted).first()
            if not job:
                return Response({'error': 'Job not found '}, 
                                status=status.HTTP_404_NOT_FOUND)
            
            # Update the specified field
            setattr(job, update_field, update_value)
            job.save()

            return Response({'success': f'{update_field.capitalize()} updated successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating job statistics: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    
    # deleting a job statistics
    def delete(self,request):
        try:
          user = request.user
          if not user.is_company:
                return Response({'error': 'User does not have permission to delete a job statistics'}, 
                                status=status.HTTP_403_FORBIDDEN)
          
          data = request.data
          job_title = data['job_title']
          company_name = data['company_name']
          date_posted = data['date_posted']
          if not analytics.objects.filter(company_email=user.email,job_title=job_title, company_name=company_name,date_posted=date_posted ).exists():
              return Response(
                  {'error':'Job ststistics that you are trying to delete does not exists'},
                  status=status.HTTP_404_NOT_FOUND
              )
          analytics.objects.filter(company_email=user.email, job_title=job_title, company_name=company_name,date_posted=date_posted).delete()

          if not analytics.objects.filter(company_email=user.email, company_name=company_name,date_posted=date_posted).exists():
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
        
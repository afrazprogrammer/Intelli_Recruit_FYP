from django.shortcuts import render
from rest_framework.views import APIView
from .models import jobinterview, int_evaluation
from rest_framework import status, permissions
from rest_framework.response import Response
import datetime
from .serializer import interviewSerializer, evaluationSerializer
from django.contrib.postgres.search import SearchVector, SearchQuery
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db.models import Q
from datetime import datetime
from django.db import IntegrityError


##################### job interview database views ###########################
# for job applicant side
class interviewApplicantView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            interview_list = None

            # Get parameters from request
            job_title = request.query_params.get('job_title')
            company_email = request.query_params.get('company_email')
            job_posted_date = request.query_params.get('job_posted_date')

            # Check if the user is a company user and has the necessary permissions
            if not user.is_company:
                # Retrieve interview details only if the applicant email matches the current user's email
                interview_list = jobinterview.objects.filter(
                    applicant_email=user.email,
                    job_title=job_title,
                    company_email=company_email,
                    job_posted_date=job_posted_date
                )
            else:
                return Response({'error': 'User does not have necessary permissions for getting this interview details'}, status=status.HTTP_403_FORBIDDEN)

            serializer = interviewSerializer(interview_list, many=True)
            return Response({'interview_details': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong while retrieving the interview details: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self, data):
        company_email = data['company_email'].lower()
        job_title = data['job_title']  # Ensure job_title is extracted
        job_posted_date = data.get('job_posted_date')
        applicant_first_name = data.get('applicant_first_name')
        applicant_last_name = data.get('applicant_last_name')
        question = data.get('question')
        answer = data.get('answer')
        date = data.get('date')
        
        # Ensure date is provided and not null
        if date is None:
            raise ValueError('Missing or null value for the "date" field.')
        
        # Ensure date is in the correct format
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Incorrect date format. Please use YYYY-MM-DD format for date.')
        
        data = {
            'company_email': company_email,
            'job_title': job_title,  # Include job_title in the data dictionary
            'job_posted_date': job_posted_date,
            'applicant_first_name': applicant_first_name,
            'applicant_last_name': applicant_last_name,
            'question': question,
            'answer': answer,
            'date': date
        }
        
        return data

    
    def post(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User does not have permission to create a job'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            
            # Set the applicant_email field using the user's email
            data['applicant_email'] = user.email
            
            int_serializer = interviewSerializer(data=data)
            if int_serializer.is_valid():
                int_serializer.save()
                return Response({'success': 'Interview detail added successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(int_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': f'Something went wrong when adding an interview detail: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# for company
class interviewCompanyView(APIView):
   def get(self, request, format=None):
        try:
            user = request.user
            interview_list = None

            # Get parameters from request
            job_title = request.query_params.get('job_title')
            job_posted_date = request.query_params.get('job_posted_date')

            if user.is_company:
                # Company users can view interview details filtered by job title, posted date, and company email
                company_email = user.email
                interview_list = jobinterview.objects.filter(job_title=job_title, company_email=company_email,  job_posted_date=job_posted_date)
            else:
                return Response({'error': 'User does not have necessary permissions for getting this interview details'}, status=status.HTTP_403_FORBIDDEN)

            serializer = interviewSerializer(interview_list, many=True)
            return Response({'interview_details': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong while retrieving the interview details: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # deleting a job interview 
   def delete(self, request, format=None):
        try:
            user = request.user

            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)

            # Get parameters from request
            job_title = request.query_params.get('job_title')
            posted_date = request.query_params.get('posted_date')

            # Filter interview details by job title, posted date, and company email
            company_email = user.email
            interview_details = jobinterview.objects.filter(job_title=job_title, job_posted_date=posted_date, company_email=company_email)

            if not interview_details.exists():
                return Response({'error': 'Interview details not found'}, status=status.HTTP_404_NOT_FOUND)

            # Delete interview details
            interview_details.delete()

            return Response({'message': 'Interview details deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'error': f'Something went wrong while deleting interview details: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################### interview evaluation views ###########################################
class evaluationView(APIView):
   def get(self, request, format=None):
        try:
            user = request.user

            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)

            # Get parameters from request
            job_title = request.query_params.get('job_title')
            applicant_email = request.query_params.get('applicant_email')
            job_posted_date = request.query_params.get('job_posted_date')
            interview_date = request.query_params.get('interview_date')

            # Filter evaluation details based on parameters and company email
            company_email = user.email
            evaluation_details = int_evaluation.objects.filter(
                job_title=job_title,
                applicant_email=applicant_email,
                interview_date=interview_date,  
                company_email=user.email
            )

            serializer = evaluationSerializer(evaluation_details, many=True)
            return Response({'evaluation_details': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong while retrieving evaluation details: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # details in evaluation database will be added from the applicant side
  

   def post(self, request, format=None):
        try:
            user = request.user

            # Check if the user is a company
            if user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)

            # Deserialize the request data
            serializer = evaluationSerializer(data=request.data)

            if serializer.is_valid():
                # Check if the evaluation data already exists
                existing_evaluation = int_evaluation.objects.filter(
                    applicant_email=user.email,
                    job_title=serializer.validated_data['job_title'],
                    interview_date=serializer.validated_data['interview_date']
                ).exists()

                if existing_evaluation:
                    return Response({'error': 'Evaluation data already exists for this user, job title, and interview date'}, status=status.HTTP_400_BAD_REQUEST)

                # Save the evaluation data to the database
                serializer.save(applicant_email=user.email)  # Assign the company email to the serializer data
                return Response({'success': 'Evaluation data saved successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': f'Something went wrong while saving evaluation data: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


   def delete(self, request, format=None):
        try:
            user = request.user

            # Check if the user is a company
            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)

            # Get parameters from request
            job_title = request.query_params.get('job_title')
            job_posted_date = request.query_params.get('job_posted_date')

            # Filter evaluation details by job title, job posted date, and company email
            evaluation_details = int_evaluation.objects.filter(
                job_title=job_title,
                job_posted_date=job_posted_date,
                company_email=user.email
            )

            # Check if the evaluation details exist
            if not evaluation_details.exists():
                return Response({'error': 'Evaluation details not found'}, status=status.HTTP_404_NOT_FOUND)

            # Delete the evaluation details
            evaluation_details.delete()

            return Response({'message': 'Evaluation details deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'error': f'Something went wrong while deleting evaluation details: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





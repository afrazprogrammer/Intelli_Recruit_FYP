from django.shortcuts import render
from rest_framework.views import APIView
from .models import Company, CompanyProjects, CompanyLocation, JobSeeker, Skill, Project
from rest_framework import status, permissions
from rest_framework.response import Response
import datetime
from .serializer import companySerializer, complocSerializer, comprojSerializer, jobseekerSerializer, skillSerializer, projSerializer
from django.contrib.postgres.search import SearchVector, SearchQuery
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db.models import Q
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

### for company profile
class compView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user

            if user.is_company:
                # Company user can view its own profile only
                profile = Company.objects.filter(email=user.email)
            else:
                # Non-company user can view the profile with a specific email
                requested_email = request.query_params.get('email')
                if not requested_email:
                    return Response({'error': 'Email parameter is required for non-company users'}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                profile = Company.objects.filter(email=requested_email)

            profile_info = companySerializer(profile, many=True)
            return Response({'listss': profile_info.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong while retrieving company profile information: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def retrieve_values(self,data):
        name = data['name']
        email = data['email']
        email = email.lower()
        contact_no = data['contact_no']
        about = data.get('about')
        min_salary_offered = data['min_salary_offered']
        company_picture = data['company_picture']
        instagram_account = data['instagram_account']
        facebook_account = data['facebook_account']
        linkedin_profile = data['linkedin_profile']

        data = {
            'name': name,
            'email': email,
            'contact_no': contact_no,
            'about': about, 
            'min_salary_offered': min_salary_offered,
            'company_picture': company_picture,
            'instagram_account': instagram_account,
            'facebook_account': facebook_account,
            'linkedin_profile': linkedin_profile,

}
        return data

    # add different details to the profile
    def post(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User does not have permission '}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            # Add the new fields to the data dictionary
            name = data['name']
            email = data['email']
            email = email.lower()
            contact_no = data['contact_no']
            about = data.get('about')
            min_salary_offered = data['min_salary_offered']
            company_picture = data['company_picture']
            instagram_account = data['instagram_account']
            facebook_account = data['facebook_account']
            linkedin_profile = data['linkedin_profile']

            # Check if required fields are present
            required_fields = ['name', 'email', 'contact_no', 'min_salary_offered', 'about','company_picture', 'instagram_account', 'facebook_account', 'linkedin_profile']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
             
            # Check if profilee with the same email and company name already exists
            if Company.objects.filter(name=name,email=email).exists():
                return Response({'error': 'Profile of the company already exists'}, 
                                status=status.HTTP_400_BAD_REQUEST)
            
            # Create job
            profile = Company.objects.create(
                 name = name,
                 email = email,
                 contact_no = contact_no,
                 about = about,
                 min_salary_offered = min_salary_offered,
                 company_picture = company_picture,
                 instagram_account = instagram_account,
                 facebook_account = facebook_account,
                 linkedin_profile = linkedin_profile,
            )

            return Response({'success': 'Company Profile created Successfully'}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating a company profile: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update the information in the profile
    def put(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            profile = Company.objects.filter(email=user.email).first()
            if not profile:
                return Response({'error': 'Company profile not found'}, status=status.HTTP_404_NOT_FOUND)

            data = self.retrieve_values(data)
            profile.name = data.get('name', profile.name)
            profile.contact_no = data.get('contact_no', profile.contact_no)
            profile.about = data.get('about', profile.about)
            profile.min_salary_offered = data.get('min_salary_offered', profile.min_salary_offered)
            profile.company_picture = data.get('company_picture', profile.company_picture)
            profile.instagram_account = data.get('instagram_account', profile.instagram_account)
            profile.facebook_account = data.get('facebook_account', profile.facebook_account)
            profile.linkedin_profile = data.get('linkedin_profile', profile.linkedin_profile)
            profile.save()

            return Response({'success': 'Company Profile updated Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating company profile: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # deleting a profile
    def delete(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            profile = Company.objects.filter(email=user.email).first()
            if not profile:
                return Response({'error': 'Company profile not found'}, status=status.HTTP_404_NOT_FOUND)

            profile.delete()

            return Response({'success': 'Company Profile deleted Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting company profile: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



### for company locations, different addresses
class complocView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            if user.is_company:
                # Company user can view all  of its locations
                profile = CompanyLocation.objects.filter(email=user.email)
            else:
                # Non-company user can view the profile with a specific email
                requested_email = request.query_params.get('email')
                if not requested_email:
                    return Response({'error': 'Email parameter is required for non-company users'}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                profile = CompanyLocation.objects.filter(email=requested_email)

            profile_info = complocSerializer(profile, many=True)
            return Response({'listss': profile_info.data}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving company location information'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self,data):
        email = data['email']
        email = email.lower()
        address = data['address']
        city = data['city']
        country = data['country']

        data = {
            'email': email,
            'address': address,
            'city': city, 
            'country': country,

}
        return data

    # add different details to the profile
    def post(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User does not have permission '}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            email = data['email']
            email = email.lower()
            address = data['address']
            city = data['city']
            country = data['country']


            # Check if required fields are present
            required_fields = ['email', 'address', 'city', 'country']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
            
            loc = CompanyLocation.objects.create(
                 email = email,
                 address = address,
                 city = city,
                 country = country,
            )

            return Response({'success': 'Company Location information created Successfully'}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating a company locations information: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update the information in the locations
    def put(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            profile = CompanyLocation.objects.filter(email=user.email)
            if not profile:
                return Response({'error': 'Company Location detail not found'}, status=status.HTTP_404_NOT_FOUND)

            data = self.retrieve_values(data)
            profile.address= data.get('address', profile.address)
            profile.city = data.get('city', profile.city)
            profile.country = data.get('country', profile.country)
            profile.save()

            return Response({'success': 'Company Location informaiton updated Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating company Locations: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # deleting a company location
    def delete(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            profile = CompanyLocation.objects.filter(email=user.email).first()
            if not profile:
                return Response({'error': 'Company Location information not found'}, status=status.HTTP_404_NOT_FOUND)

            profile.delete()

            return Response({'success': 'Company Location deleted Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting company location: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


### from company different projects
class comprojView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            if user.is_company:
                # Company user can view all of its projects
                profile = CompanyProjects.objects.filter(email=user.email)
            else:
                # Non-company user can view the projects with a specific email
                requested_email = request.query_params.get('email')
                if not requested_email:
                    return Response({'error': 'Email parameter is required for non-company users'}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                profile = CompanyProjects.objects.filter(email=requested_email)


            profile_info = comprojSerializer(profile, many=True)
            return Response({'listss': profile_info.data}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving company project information'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self, data):
        email = data['email']
        email=email.lower()  # Get email, allow None
        project_name = data['project_name']
        project_duration = data['project_duration']
        client_name = data['client_name']
        project_description = data['project_description']


        data= {
            'email': email,
            'project_name': project_name,
            'project_duration': project_duration,
            'client_name': client_name,
            'project_description': project_description,
        }

        return data

    # add different details to the profile
    def post(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User does not have permission '}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            email = data['email']
            email=email.lower()  # Get email, allow None
            project_name = data['project_name']
            project_duration = data['project_duration']
            client_name = data['client_name']
            project_description = data['project_description']

            # Check if required fields are present
            required_fields = ['project_name', 'project_duration', 'client_name', 'project_description']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
            
            loc = CompanyProjects.objects.create(
                 email= email,
                 project_name=project_name,
                 project_duration=project_duration,
                 client_name=client_name,
                 project_description=project_description,
            )

            return Response({'success': 'Company projects information created Successfully'}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating a company projects information: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update the information in the profile
    def put(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            profile = CompanyProjects.objects.get(email=user.email)
            if not profile:
                return Response({'error': 'Company project detail not found'}, status=status.HTTP_404_NOT_FOUND)

            profile.project_name = data.get('project_name', profile.project_name)
            profile.project_duration = data.get('project_duration', profile.project_duration)
            profile.project_description = data.get('project_description', profile.project_description)
            profile.client_name = data.get('client_name', profile.client_name)
            profile.save()

            return Response({'success': 'Company projects informaiton updated Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating company project: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # deleting a company location
    def delete(self, request):
        try:
            user = request.user
            if not user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            project_name = request.query_params.get('project_name')
            if project_name:
                # Delete the project with the specified name belonging to the user
                project = CompanyProjects.objects.filter(email=user.email, project_name=project_name).first()
                if not project:
                    return Response({'error': 'Project not found for this user'}, status=status.HTTP_404_NOT_FOUND)
                project.delete()
            else:
                # Delete all projects associated with the user
                CompanyProjects.objects.filter(email=user.email).delete()

            return Response({'success': 'Projects deleted Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting projects: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


### for job seeker profile
class jobseekerView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            if not user.is_company:
                profile = JobSeeker.objects.filter(email=user.email)
            else:
                 # company user can view the profile with a specific email
                requested_email = request.query_params.get('email')
                if not requested_email:
                    return Response({'error': 'Email parameter is required for company users'}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                profile = JobSeeker.objects.filter(email=requested_email)

            profile_info = jobseekerSerializer(profile, many=True)
            return Response({'listss': profile_info.data}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving company profile information'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self, data):
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        cnic = data['cnic']
        date_of_birth = data['date_of_birth']
        address = data['address']
        province = data['province']
        city = data['city']
        country = data['country']
        phone_no = data['phone_no']
        zip_code = data['zip_code']
        about_you = data['about_you']
        education = data['education']
        cgpa = data['cgpa']
        profile_link = data['profile_link']
        experience_years = data['experience_years']
        awards = data['awards']
        certificates = data['certificates']

        # Ensure date_of_birth is provided and not null
        if date_of_birth is None:
            raise ValueError('Missing or null value for the "date_of_birth" field.')
        
        # Ensure date_of_birth is in the correct format
        try:
            date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Incorrect date format. Please use YYYY-MM-DD format for date_of_birth.')

        data = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'cnic': cnic,
            'date_of_birth': date_of_birth,
            'address': address,
            'province': province,
            'city': city,
            'country': country,
            'phone_no': phone_no,
            'zip_code': zip_code,
            'about_you': about_you,
            'education': education,
            'cgpa': cgpa,
            'profile_link': profile_link,
            'experience_years': experience_years,
            'awards': awards,
            'certificates': certificates
        }
        
        return data


    # add different details to the profile
    def post(self, request):
        try:
            user = request.user
            if  user.is_company:
                return Response({'error': 'User does not have permission '}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            # Add the new fields to the data dictionary
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            cnic = data['cnic']
            date_of_birth = data['date_of_birth']
            address = data['address']
            province = data['province']
            city = data['city']
            country = data['country']
            phone_no = data['phone_no']
            zip_code = data['zip_code']
            about_you = data['about_you']
            education = data['education']
            cgpa = data['cgpa']
            profile_link = data['profile_link']
            experience_years = data['experience_years']
            awards = data['awards']
            certificates = data['certificates']

            # Check if required fields are present
            required_fields = ['email', 'first_name', 'last_name', 'cnic', 'date_of_birth', 'address', 'province', 'city', 'country', 'phone_no', 'zip_code', 'about_you', 'education', 'cgpa', 'profile_link', 'experience_years', 'awards', 'certificates']

            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
             
            # Check if profile with the same email and name already exists
            if JobSeeker.objects.filter(first_name=first_name,last_name=last_name,email=email).exists():
                return Response({'error': 'Profile of the Job Seeker already exists'}, 
                                status=status.HTTP_400_BAD_REQUEST)
            
            # Create profile
            profile = JobSeeker.objects.create(
                email = email,
                first_name = first_name,
                last_name = last_name,
                cnic = cnic,
                date_of_birth = date_of_birth,
                address = address,
                province = province,
                city = city,
                country = country,
                phone_no = phone_no,
                zip_code = zip_code,
                about_you = about_you,
                education = education,
                cgpa = cgpa,
                profile_link = profile_link,
                experience_years = experience_years,
                awards = awards,
                certificates = certificates

            )

            return Response({'success': 'Job Seeker Profile created Successfully'}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating a Job seeker profile: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update the information in the profile
    def put(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            profile = JobSeeker.objects.filter(email=user.email).first()
            if not profile:
                return Response({'error': 'Job seeker profile not found'}, status=status.HTTP_404_NOT_FOUND)

            data = self.retrieve_values(data)
            profile.first_name = data.get('first_name', profile.first_name)
            profile.last_name = data.get('last_name', profile.last_name)
            profile.cnic = data.get('cnic', profile.cnic)
            profile.date_of_birth = data.get('date_of_birth', profile.date_of_birth)
            profile.address = data.get('address', profile.address)
            profile.province = data.get('province', profile.province)
            profile.city = data.get('city', profile.city)
            profile.country = data.get('country', profile.country)
            profile.phone_no = data.get('phone_no', profile.phone_no)
            profile.zip_code = data.get('zip_code', profile.zip_code)
            profile.about_you = data.get('about_you', profile.about_you)
            profile.education = data.get('education', profile.education)
            profile.cgoa = data.get('cgpa', profile.cgpa)
            profile.profile_link = data.get('profile_link', profile.profile_link)
            profile.experience_years = data.get('experience_years', profile.experience_years)
            profile.awards = data.get('awards', profile.awards)
            profile.certificates = data.get('certificates', profile.certificates)
            profile.save()

            return Response({'success': ' Job seeker Profile updated Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating job seeker profile: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # deleting a profile
    def delete(self, request):
        try:
            user = request.user
            if  user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            profile = JobSeeker.objects.filter(email=user.email).first()
            if not profile:
                return Response({'error': 'Job seeker profile not found'}, status=status.HTTP_404_NOT_FOUND)

            profile.delete()

            return Response({'success': 'Job seeker Profile deleted Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting Job seeker profile: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


### for job seeker skills
class skillView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            if not user.is_company:
                # user can view all skills posted by itself
                profile = Skill.objects.filter(email=user.email)
            else:
              #company user can view the skill with a specific email
                requested_email = request.query_params.get('email')
                if not requested_email:
                    return Response({'error': 'Email parameter is required for company users'}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                profile = Skill.objects.filter(email=requested_email)

            profile_info = skillSerializer(profile, many=True)
            return Response({'listss': profile_info.data}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving job seeker skills'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self,data):
        email = data['email']
        email = email.lower()
        cnic = data['cnic']
        ### skill name
        name = data['name']

        data = {
            'email': email,
            'cnic': cnic,
            'name': name, 

}
        return data

    # add different details to the profile
    def post(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User does not have permission '}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            email = data['email']
            email = email.lower()
            cnic = data['cnic']
            ### skill name
            name = data['name']


            # Check if required fields are present
            required_fields = ['email', 'cnic', 'name']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
            
            loc = Skill.objects.create(
                 email = email,
                 cnic = cnic,
                 name = name,
            )

            return Response({'success': 'Job seeker skills information created Successfully'}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating job seeker skills information: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            name = request.query_params.get('name')
            if name:
                # Delete the skill with the specified name and belonging to the user
                skill = Skill.objects.filter(email=user.email, name=name).first()
                if not skill:
                    return Response({'error': 'Skill not found for this user'}, status=status.HTTP_404_NOT_FOUND)
                skill.delete()
            else:
                # Delete all skills associated with the user
                Skill.objects.filter(email=user.email).delete()

            return Response({'success': 'Skills deleted Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting job seeker skills: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


### for job seeker projects
class projView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            job_list = None

            if not user.is_company:
                #  user can view all of its projects
                profile = Project.objects.filter(email=user.email)
            else:
                # company user can view the projects with a specific email
                requested_email = request.query_params.get('email')
                if not requested_email:
                    return Response({'error': 'Email parameter is required for non-company users'}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                profile = Project.objects.filter(email=requested_email)


            profile_info = projSerializer(profile, many=True)
            return Response({'listss': profile_info.data}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Something went wrong while retrieving job seeker projects'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self, data):
        email = data['email']
        email=email.lower()  # Get email, allow None
        company = data['company']
        project_name = data['project_name']
        project_duration = data['project_duration']
        role = data['role']
        description = data['description']


        data= {
            'email': email,
            'company':company,
            'project_name': project_name,
            'project_duration': project_duration,
            'role': role,
            'description': description,
        }

        return data

    # add different details to the profile
    def post(self, request):
        try:
            user = request.user
            if  user.is_company:
                return Response({'error': 'User does not have permission '}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            data = self.retrieve_values(data)
            email = data['email']
            email=email.lower()  # Get email, allow None
            project_name = data['project_name']
            company = data['company']
            project_duration = data['project_duration']
            role= data['role']
            description = data['description']

            # Check if required fields are present
            required_fields = ['project_name', 'project_duration', 'role','company', 'description']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
            
            loc = Project.objects.create(
                 email= email,
                 project_name=project_name,
                 project_duration=project_duration,
                 company = company,
                 role=role,
                 description=description,
            )

            return Response({'success': 'Job applicant projects information created Successfully'}, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Something went wrong when creating an applicant projects information: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update the information in the profile
    def put(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            project_title = data.get('project_title')
            if not project_title:
                return Response({'error': 'Project title is required'}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the project associated with the provided title and user's email
            try:
                project = Project.objects.get(email=user.email, project_name=project_title)
            except ObjectDoesNotExist:
                return Response({'error': 'Project not found for this user'}, status=status.HTTP_404_NOT_FOUND)

            # Update project details
            project.project_duration = data.get('project_duration', project.project_duration)
            project.description = data.get('description', project.description)
            project.role = data.get('role', project.role)
            project.company = data.get('company', project.company)
            project.save()

            return Response({'success': 'Project information updated successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating project: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # deleting a company location
    def delete(self, request):
        try:
            user = request.user
            if user.is_company:
                return Response({'error': 'User is not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            
            project_name = request.query_params.get('project_name')
            if project_name:
                # Delete the project with the specified project name and belonging to the user
                project = Project.objects.filter(email=user.email, project_name=project_name).first()
                if not project:
                    return Response({'error': 'Project not found for this user'}, status=status.HTTP_404_NOT_FOUND)
                project.delete()
            else:
                # Delete all projects associated with the user
                Project.objects.filter(email=user.email).delete()

            return Response({'success': 'Projects deleted Successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting projects: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


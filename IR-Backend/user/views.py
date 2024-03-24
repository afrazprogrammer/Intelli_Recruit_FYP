from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model
from .serializer import UserSerializer

User = get_user_model()

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data
            required_fields = ['name', 'email', 'password', 're_password', 'is_company']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            is_company = data['is_company']

            if is_company.lower() == 'true':
                is_company = True
            else:
                is_company = False

            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_company:
                            User.objects.create_user(name=name, email=email, password=password)
                            return Response({'success': 'Job seeker account created successfully'}, status=status.HTTP_201_CREATED)
                        else:
                            User.objects.create_company(name=name, email=email, password=password)
                            return Response({'success': 'Company account created successfully'}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'error': "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': "Password must be at least 8 characters in length"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Something went wrong when registering an account'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {'error': 'Something went wrong while retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

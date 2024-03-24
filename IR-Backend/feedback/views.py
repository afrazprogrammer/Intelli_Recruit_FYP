from django.shortcuts import render
from rest_framework.views import APIView
from .models import comments
from rest_framework import status, permissions
from rest_framework.response import Response
import datetime
from .serializer import commentSerializer


class commentView(APIView):
    def get(self, request, format=None):
        try:
            comments_list = comments.objects.order_by('-created_at')
            comments_serializer = commentSerializer(comments_list, many=True)
            return Response({'comments': comments_serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Something went wrong while retrieving the comments'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve_values(self, data):
        user_email = data.get('user_email')
        user_name = data.get('user_name')
        comment = data.get('comment')
        
        # Automatically add the present date and time
        date_time_posted = datetime.datetime.now()

        # Ensure user_email is lowercased
        if user_email:
            user_email = user_email.lower()

        # Construct the data dictionary
        comment_data = {
            'user_email': user_email,
            'user_name': user_name,
            'comment': comment,
            'date_time_posted': date_time_posted,
        }
        
        return comment_data


    
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['user_email'] = user.email  # Assuming the user's email is stored in the 'email' field
            
            if 'user_name' not in data:
                data['user_name'] = user.username  # Assuming the user's name is stored in the 'username' field
            
            data = self.retrieve_values(data)

            # Check if required fields are present
            required_fields = ['user_email', 'user_name', 'comment']
            if not all(field in data for field in required_fields):
                return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

            # Create comment
            comment_serializer = commentSerializer(data=data)
            if comment_serializer.is_valid():
                comment_serializer.save()
                return Response({'success': 'Comment posted successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': f'Something went wrong when posting a comment: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            

    # to update a piece or data, to update the status of the job whether the company is hiring or is filled
    def patch(self, request):
        try:
            user = request.user
            data = request.data
            comment_id = data.get('id')
            new_comment_text = data.get('comment')

            if not comment_id or not new_comment_text:
                return Response({'error': 'Comment ID and new comment text are required'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the comment exists and belongs to the user
            comment = comments.objects.filter(id=comment_id, user_email=user.email).first()

            if not comment:
                return Response({'error': 'Comment not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)

            # Update the comment text
            comment.comment = new_comment_text
            comment.save()

            return Response({'success': 'Comment updated successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Something went wrong when updating the comment: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    
    def delete(self, request):
        try:
            user = request.user
            data = request.data
            comment_id = data.get('id')

            if not comment_id:
                return Response({'error': 'Comment ID is required'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the comment exists and belongs to the user
            comment = comments.objects.filter(id=comment_id, user_email=user.email).first()

            if not comment:
                return Response({'error': 'Comment not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)

            # Delete the comment
            comment.delete()

            return Response({'success': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'error': f'Something went wrong when deleting the comment: {e}'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

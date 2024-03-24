from .models import comments

def delete_comments_listing_data(user_email):
    if comments.objects.filter(user_email=user_email).exists():
        comments.objects.filter(user_email=user_email).delete()
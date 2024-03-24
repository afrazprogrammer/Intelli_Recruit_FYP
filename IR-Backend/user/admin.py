from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
from application.extras import delete_savedjobs_listing_data, delete_statistics_listing_data
from feedback.extras import delete_comments_listing_data
from interview.extras import delete_evaluation_listing_data, delete_interview_listing_data
from jobs.extras import delete_jobs_listing_data
from Profile.extras import delete_applicant_listing_data, delete_company_listing_data, delete_comproj_listing_data, delete_loc_listing_data, delete_proj_listing_data, delete_skill_listing_data


class UserAdmin(admin.ModelAdmin):
    using = 'irusers'
    list_display = ('id', 'name', 'email', )
    list_display_links = ('id', 'name', 'email', )
    search_fields = ('name', 'email', )
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        email = obj.email
        obj.delete(using=self.using)

        # when the user gets deleted so of the user is 
        # job applicant than its information from the profile
        # will be deleted and if the user is company then all the jobs
        # posted by it and all the job related data will be deleted.
        delete_skill_listing_data(email)
        delete_applicant_listing_data(email)
        delete_comments_listing_data(email)
        delete_company_listing_data(email)
        delete_comproj_listing_data(email)
        delete_loc_listing_data(email)
        delete_proj_listing_data(email)
        delete_interview_listing_data(email)
        delete_evaluation_listing_data(email)
        delete_savedjobs_listing_data(email)
        delete_statistics_listing_data(email)
        delete_jobs_listing_data(email)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

admin.site.register(User, UserAdmin)
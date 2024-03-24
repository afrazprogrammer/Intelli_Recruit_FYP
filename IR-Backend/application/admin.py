from django.contrib import admin
from .models import saved_jobs, analytics


class savedJOBAdmin(admin.ModelAdmin):
    using = 'saved_jobs'
    list_display = ('id', 'company_email', 'company_name', 'job_title','date_posted','user_email' )
    list_display_links = ('id', 'company_email', 'company_name', 'job_title','date_posted','user_email' )
    list_filter = ('user_email','job_title' )
    search_fields = ('title', 'company_name', )
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
    

class jobstatisticsAdmin(admin.ModelAdmin):
    using = 'analytics'
    list_display = ('id', 'company_email', 'company_name', 'job_title','date_posted','views','applied','saved' )
    list_display_links = ('id', 'company_email', 'company_name', 'job_title','date_posted','views','applied','saved' )
    list_filter = ('company_email','job_title' )
    search_fields = ('job_title', 'company_name', )
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

admin.site.register(saved_jobs, savedJOBAdmin)
admin.site.register(analytics, jobstatisticsAdmin)
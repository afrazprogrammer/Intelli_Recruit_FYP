from django.contrib import admin
from .models import jobinterview, int_evaluation


class interviewAdmin(admin.ModelAdmin):
    using = 'jobinterview'
    list_display = ('id', 'company_email', 'job_title','date','applicant_email' )
    list_display_links = ('id', 'company_email', 'job_title','date','applicant_email' )
    list_filter = ('applicant_email','job_title' )
    search_fields = ('job_title', 'company_email', )
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
    

class evaluationAdmin(admin.ModelAdmin):
    using = 'int_evaluation'
    list_display = ('id', 'company_email', 'job_title','applicant_email' )
    list_display_links = ('id', 'company_email', 'job_title','applicant_email' )
    list_filter = ('job_title', 'company_email' )
    search_fields = ('job_title', 'company_email', )
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

admin.site.register(jobinterview, interviewAdmin)
admin.site.register(int_evaluation, evaluationAdmin)

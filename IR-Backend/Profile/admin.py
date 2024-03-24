from django.contrib import admin
from .models import Company, JobSeeker, CompanyLocation, CompanyProjects, Skill, Project


class compAdmin(admin.ModelAdmin):
    using = 'ircompany'
    list_display = ('id', 'email', 'name','contact_no' )
    list_display_links = ('id', 'email', 'name','contact_no' )
    list_filter = ('email','name' )
    search_fields = ('name', 'email', )
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
    

class applicantionAdmin(admin.ModelAdmin):
    using = 'jobseeker'
    list_display = ('id', 'email', 'first_name','last_name','cnic' )
    list_display_links = ('id', 'email', 'first_name','last_name','cnic' )
    list_filter = ('email', 'first_name' )
    search_fields = ('email', 'first_name' )
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


class comprojAdmin(admin.ModelAdmin):
    using = 'companyprojects'
    list_display = ('id', 'email', 'project_name','client_name')
    list_display_links = ('id', 'email', 'project_name','client_name')
    list_filter = ('email', 'client_name' )
    search_fields = ('email', 'client_name' )
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


class complocAdmin(admin.ModelAdmin):
    using = 'companylocations'
    list_display = ('id', 'email', 'city','country' )
    list_display_links = ('id', 'email', 'city','country' )
    list_filter = ('email', 'country' )
    search_fields = ('email', 'country' )
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


class skillAdmin(admin.ModelAdmin):
    using = 'skillss'
    list_display = ('id', 'email', 'name' )
    list_display_links = ('id', 'email', 'name' )
    list_filter = ('email', 'name' )
    search_fields = ('email', 'name' )
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


class projectAdmin(admin.ModelAdmin):
    using = 'jobseekerprojects'
    list_display = ('id', 'email', 'company','project_name' )
    list_display_links = ('id', 'email', 'company','project_name' )
    list_filter = ('email', 'company' )
    search_fields = ('email', 'company' )
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


admin.site.register(Company, compAdmin)
admin.site.register(JobSeeker, applicantionAdmin)
admin.site.register(CompanyLocation, complocAdmin)
admin.site.register(CompanyProjects, comprojAdmin)
admin.site.register(Skill,skillAdmin)
admin.site.register(Project, projectAdmin)
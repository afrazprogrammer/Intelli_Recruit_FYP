from django.contrib import admin
from .models import comments


class commentAdmin(admin.ModelAdmin):
    using = 'comments'
    list_display = ('id',  'user_email','user_name','comment','created_at' )
    list_display_links = ('id',  'user_email','user_name','comment','created_at' )
    list_filter = ('user_email','user_name' )
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
    
admin.site.register(comments, commentAdmin)

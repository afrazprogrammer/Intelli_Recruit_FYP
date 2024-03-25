from django.contrib import admin
from .models import Company, JobSeeker, Education, WorkExp, Jobs, JobsSaved, Interviews, Feedback
# Register your models here.
admin.site.register(Company)
admin.site.register(JobSeeker)
admin.site.register(Education)
admin.site.register(WorkExp)
admin.site.register(Jobs)
admin.site.register(JobsSaved)
admin.site.register(Interviews)
admin.site.register(Feedback)
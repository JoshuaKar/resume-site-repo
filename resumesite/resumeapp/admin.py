from django.contrib import admin
from .models import Education, Skills, Work, Projects
# Register your models here.

admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Work)
admin.site.register(Projects)
from django.contrib import admin
from .models import home, project, referees, New_Messages, services

# Register your models here.
admin.site.register(home)
admin.site.register(project)
admin.site.register(referees)
admin.site.register(New_Messages)
admin.site.register(services)
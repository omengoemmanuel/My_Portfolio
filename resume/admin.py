from django.contrib import admin
from .models import home, project, referees, New_Messages, servicess, blogs,works,portfolios, work_done_details, feedback

# Register your models here.
admin.site.register(home)
admin.site.register(project)
admin.site.register(referees)
admin.site.register(New_Messages)
admin.site.register(servicess)
admin.site.register(blogs)
admin.site.register(works)
admin.site.register(portfolios)
admin.site.register(work_done_details)
admin.site.register(feedback)
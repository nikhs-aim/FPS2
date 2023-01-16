from django.contrib import admin
from .models import Faculty
from .models import Conference,Journal

admin.site.register(Conference)
admin.site.register(Journal)
admin.site.register(Faculty)



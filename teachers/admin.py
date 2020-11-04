from django.contrib import admin
from .models import Teacher,Gender,Subject
# Register your models here.

admin.site.register(Subject)
admin.site.register(Gender)
admin.site.register(Teacher)
from django.contrib import admin

# Register your models here.
from .models import Task

class task(admin.ModelAdmin):
    list_display= ('user', 'title', 'complete', 'created')

admin.site.register(Task,task)
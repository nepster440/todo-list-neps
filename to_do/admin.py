from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')  # Show in Admin Panel

admin.site.register(Task, TaskAdmin)
# Register your models here.

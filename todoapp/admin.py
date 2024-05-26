"""
admin module
"""

from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """
    Taskadmin for admin page
    """
    list_display = ('title', 'description', 'stage', 'created_at')
    list_filter = ('stage',)
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

admin.site.register(Task, TaskAdmin)



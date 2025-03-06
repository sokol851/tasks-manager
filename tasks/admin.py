from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """ Управление задачами """
    list_display = (
        'title',
        'is_completed'
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'is_completed',
    )

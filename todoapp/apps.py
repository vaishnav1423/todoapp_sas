"""
apps module
"""
from django.apps import AppConfig


class TodoappConfig(AppConfig):
    """
    Todo app config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoapp'

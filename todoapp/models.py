"""
Model definitions
"""
from django.db import models
from django.contrib.auth.models import User

def get_admin_user():
    # fetching admins from DB
    return User.objects.get(username='admin').id

class Task(models.Model):
    """
    Task Class which will hold the db definition for each Task
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, default=get_admin_user)
    title = models.CharField(max_length=255)
    description = models.TextField()
    stage_choices = [
        ('todo', 'Todo'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]
    stage = models.CharField(max_length=10, choices=stage_choices, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title





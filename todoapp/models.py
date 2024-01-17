from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stage_choices = [
        ('todo', 'Todo'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]
    stage = models.CharField(max_length=10, choices=stage_choices, default='todo')

    def __str__(self):
        return self.title
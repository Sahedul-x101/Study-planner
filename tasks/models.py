from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)  
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    duration = models.IntegerField(blank=True, null=True, help_text="Duration in min")
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
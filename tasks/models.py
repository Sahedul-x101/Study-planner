from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)  
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    duration = models.IntegerField(blank=True, null=True, help_text="Duration in min")
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

    


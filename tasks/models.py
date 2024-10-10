from django.conf import settings
from django.db import models


class Task_post(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress','In Progress'),
        ('Completed','Completed')
    ]

    PRIORITY_CHOICES = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High')
    ]

    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Work') 

    def __str__(self):
        return self.title
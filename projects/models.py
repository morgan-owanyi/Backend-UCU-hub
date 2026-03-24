from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Project(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    technologies = models.CharField(max_length=255)
    github_link = models.URLField()
    document = models.FileField(upload_to='projects/docs/')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class User (models.Model):
    
    app_label = 'dashboard'

    name = models.CharField(max_length=256)
    rollno = models.CharField(max_length=256)
    branch = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    skills = models.TextField()
    reason = models.TextField()
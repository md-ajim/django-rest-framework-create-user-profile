from django.db import models
from django.contrib.auth.models import User




class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True, default='New York')
    birthdate = models.DateField(null=True, blank=True)
 

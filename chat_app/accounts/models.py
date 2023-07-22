from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profile = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
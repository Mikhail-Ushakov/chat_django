from django.db import models
from django.contrib.auth.models import User

class ChatModel(models.Model):
    class Meta:
        ordering = ['-date']

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
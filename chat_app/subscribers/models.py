from django.db import models
from django.contrib.auth.models import User

class SubscribeModel(models.Model):
    self_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers_self_user')
    other_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers_other_user')
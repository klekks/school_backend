from django.db import models
from user.models import User
from datetime import datetime


class Event(models.Model):
    user = models.ForeignKey(User, null=True, help_text="Object of action")
    action = models.CharField(max_length=64, null=True)
    section = models.CharField(max_length=64, null=True)
    object = models.CharField(max_length=128, null=True)
    date = models.DateTimeField(default=datetime.now())
    params = models.TextField()

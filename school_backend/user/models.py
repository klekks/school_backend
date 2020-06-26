from django.db import models

class User(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

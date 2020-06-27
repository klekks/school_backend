from django.db import models
from user.models import User
from datetime import datetime


class Image(models.Model):
    image = models.ImageField(upload_to="/images")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Wallpaper(models.Model):
    image = models.ImageField(upload_to="/wallpapers")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Skin(models.Model):
    image = models.ImageField(upload_to="/wallpapers")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
from django.db import models
from utils import hash
from user.models import User
from datetime import datetime
from bcrypt import checkpw, hashpw, gensalt


class UploadUrl(models.Model):
    type = models.CharField(max_length=16)
    access = models.CharField(max_length=16, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def set_access(self):
        key = hash(16)
        self.access = key
        self.save()
        return key

    def check_access(self, key):
        return self.access == key


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Wallpaper(models.Model):
    image = models.ImageField(upload_to="wallpapers/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Skin(models.Model):
    image = models.ImageField(upload_to="wallpapers/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class File(models.Model):
    file = models.FileField(upload_to="files/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

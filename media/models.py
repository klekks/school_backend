from django.db import models
from utils import hash
from user.models import User
from datetime import datetime
from utils import get_settings
from django.core.files.images import get_image_dimensions


class UploadUrl(models.Model):
    type = models.CharField(max_length=16)
    key = models.CharField(max_length=16, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    to = models.BigIntegerField(null=True)

    def set_access(self):
        key = hash(16)
        self.key = key
        self.save()
        return key

    def check_access(self, key):
        return self.key == key

    def upload(self, file):
        hash_ = hash(16)
        file.name = hash_ + "." + file.name.split(".")[-1]
        if self.type == 'file':
            if file.size > int(get_settings("file_max_size")):
                raise ZeroDivisionError
            File(file=file, user=self.user, hash=hash_).save()
            self.delete()
        elif self.type == 'image':
            if file.size > int(get_settings("images_max_size")):
                raise ZeroDivisionError
            Image(image=file, user=self.user, hash=hash_).save()
            self.delete()
        elif self.type == 'skin':
            if file.size > int(get_settings("skin_max_size")):
                raise ZeroDivisionError
            w, h = get_image_dimensions(file)
            if int(int(w) / int(h)) != 1:
                raise InterruptedError
            skin = Skin(image=file, user=self.user, hash=hash_)
            if self.to:
                u = User.objects.get(id=self.to)
                u.skin = skin
                u.save()
                skin.save()
            skin.save()
            self.delete()
        elif self.type == "wallpaper":
            if file.size > int(get_settings("wallpaper_max_size")):
                raise ZeroDivisionError
            w, h = get_image_dimensions(file)
            k = w / h
            w = int(get_settings("wallpaper_w_ratio"))
            h = int(get_settings("wallpaper_h_ratio"))
            if round(k, 2) != round(w / h, 2):
                raise InterruptedError
            Wallpaper(image=file, user=self.user, hash=hash_).save()
            self.delete()
        if self.type == 'file':
            o = File.objects.get(hash=hash_)
            o.hash = o.file.name.split("/")[1].split(".")[0]
            o.save()
            return o.file.name
        if self.type == 'image':
            o = Image.objects.get(hash=hash_)
            o.hash = o.image.name.split("/")[1].split(".")[0]
            o.save()
            return o.image.name
        if self.type == 'wallpaper':
            o = Wallpaper.objects.get(hash=hash_)
            o.hash = o.image.name.split("/")[1].split(".")[0]
            o.save()
            return o.image.name
        if self.type == 'skin':
            o = Skin.objects.get(hash=hash_)
            o.hash = o.image.name.split("/")[1].split(".")[0]
            o.save()
            return o.image.name


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hash = models.CharField(max_length=18)

    def delete_file(self):
        storage, path = self.image.storage, self.image.path
        super(Image, self).delete()
        storage.delete(path)


class Wallpaper(models.Model):
    image = models.ImageField(upload_to="wallpapers/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hash = models.CharField(max_length=18)

    def delete_file(self):
        storage, path = self.image.storage, self.image.path
        super(Wallpaper, self).delete()
        storage.delete(path)


class Skin(models.Model):
    image = models.ImageField(upload_to="wallpapers/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hash = models.CharField(max_length=18)

    def delete_file(self):
        storage, path = self.image.storage, self.image.path
        super(Skin, self).delete()
        storage.delete(path)


class File(models.Model):
    file = models.FileField(upload_to="files/")
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hash = models.CharField(max_length=18)

    def delete_file(self):
        storage, path = self.file.storage, self.file.path
        super(File, self).delete()
        storage.delete(path)

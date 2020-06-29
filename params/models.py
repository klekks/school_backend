from django.db import models


class Settings(models.Model):
    key = models.CharField(max_length=32, unique=True)
    value = models.CharField(max_length=64)
    access = models.PositiveSmallIntegerField(default=5)

    def change_value(self, value):
        self.value = str(value)
        self.save()


class Storage(models.Model):
    key = models.CharField(max_length=32, unique=True)
    value = models.TextField()
    access = models.PositiveSmallIntegerField(default=5)

    def change_value(self, value):
        self.value = str(value)
        self.save()
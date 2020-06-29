from django.db import models
from django.db import IntegrityError
from bcrypt import hashpw, checkpw, gensalt
from datetime import datetime, timedelta
from random import randint


class User(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    salt = models.BinaryField()
    email = models.EmailField(unique=True)
    status = models.PositiveSmallIntegerField()
    logotype = models.ImageField()
    birthday = models.DateField()

    def set_password(self, password):
        self.salt = hashpw(password, gensalt())
        self.save()

    def login(self, password):
        return checkpw(password, self.salt)

    def change_name(self, name='', surname=''):
        if name or surname:
            if not name:
                self.surname = surname
            elif not surname:
                self.name = name
            else:
                self.name, self.surname = name, surname
            self.save()
            return True
        return False

    def send_mail(self):
        pass


class Temp_user(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    pin = models.BinaryField()
    status = models.PositiveSmallIntegerField()
    email = models.EmailField()
    key = models.CharField(max_length=16)
    delete_time = models.DateTimeField(default=datetime.now() + timedelta(days=1))

    def set_pin(self):
        pin = str(randint(1000, 9999))
        self.pin = hashpw(pin, gensalt())
        self.save()
        return pin

    def check_pin(self, pin):
        return checkpw(pin, self.pin)

    def create(self, params):
        try:
            user = User()
            user.name = params["name"]
            user.surname = params["surname"]
            user.email = self.email
            user.status = self.status
            user.set_password(params["password"])
            user.birthday = datetime.strptime(params["birthday"], "%d-%m-%Y %H:%M:%S")
            user.save()
            self.delete()
            return True
        except KeyError:
            return False, "Invalid Params"
        except IntegrityError:
            return False, "Already Exist"

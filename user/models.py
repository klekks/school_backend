from django.db import models
from django.db import IntegrityError
from bcrypt import hashpw, checkpw, gensalt
from datetime import datetime, timedelta, date
from random import randint
from utils import hash


class User(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    salt = models.BinaryField()
    email = models.EmailField(unique=True)
    status = models.PositiveSmallIntegerField()
    logotype = models.ImageField()
    birthday = models.DateField()
    reg = models.DateField(default=date.today())
    online = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    refer = models.ForeignKey('User', null=True, blank=True, on_delete=models.DO_NOTHING)

    def info(self, status):
        if self.status > 3:
            return {}
        data = {"name": self.name, "surname": self.surname, "status": self.status, "skin": self.logotype.name, "online": self.online}
        if status <= 1:
            data["refer"] = self.refer.name + " " + self.refer.surname
            data["refer_id"] = self.refer.id
        if status <= 3:
            data["email"] = self.email
            data["birthday"] = self.birthday
            data["registration_date"] = self.reg
        return data

    def set_password(self, password):
        self.salt = hashpw(password, gensalt())
        self.save()

    def login(self, password):
        return checkpw(password, self.salt)

    def update(self, data):
        if data.get("name", False):
            self.name = data["name"]
        if data.get("surname", False):
            self.surname = data["surname"]
        if data.get("birthday", False):
            self.birthday = datetime.strptime(data["birthday"], "%d-%m-%Y %H:%M:%S")

    def send_mail(self):
        pass


class Temp_user(models.Model):
    pin = models.BinaryField()
    status = models.PositiveSmallIntegerField()
    email = models.EmailField()
    key = models.CharField(max_length=16, default=hash(16))
    delete_time = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    refer = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def set_pin(self):
        pin = str(randint(1000, 9999))
        self.pin = hashpw(pin, gensalt())
        self.save()
        return pin

    def check_pin(self, pin):
        return checkpw(pin, self.pin)

    def create(self, params):
        user = User()
        user.name = params["name"]
        user.surname = params["surname"]
        user.email = self.email
        user.status = self.status
        user.set_password(params["password"].encode())
        user.birthday = datetime.strptime(params["birthday"], "%d-%m-%Y %H:%M:%S")
        user.refer = self.refer
        user.save()
        self.delete()

    def send_message(self):
        print("НЕ РЕАЛИЗОВАННО")


class user_updater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(default=hash(16), max_length=16)
    change = models.CharField(max_length=16)
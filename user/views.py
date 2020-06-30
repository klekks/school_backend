from utils import simple_response, hash
from django.core.validators import validate_email
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import IntegrityError
from user.models import User, Temp_user


def login(request):
    if request.method != "POST":
        return simple_response(405)
    if request.user.id == -1:
        data = request.POST
        print(request.read())
        try:
            password = data["password"]
            email = data["login"]
            validate_email(email)
            user = User.objects.get(email=email)
            if user.login(password.encode()):
                request.session["id"] = user.id
                return simple_response(200)
        except KeyError:
            print(1)
            return simple_response(400)
        except ValidationError:
            return simple_response(400)
        except ObjectDoesNotExist:
            return simple_response(401)
    else:
        return simple_response(200)


def check(request):
    print(1)
    if request.user.id == -1:
        return simple_response(401)
    else:
        return simple_response(200)


def logout(request):
    request.session.flush()
    return simple_response(200)


def user_main(request):
    if request.method == "POST":
        return add_user(request)
    elif request.method == "PUT":
        return edit_user(request)
    elif request.method == "GET":
        return get_user(request)
    elif request.method == "DELETE":
        return delete_user(request)
    return simple_response(405)


def delete_user(request):
    try:
        data = request.POST
        if request.user.status > 1:
            return simple_response(403)
        User.objects.get(id=data["id"]).delete()
        return simple_response(200)
    except KeyError:
        return simple_response(400)
    except ObjectDoesNotExist:
        return simple_response(404)


def add_user(request):
    try:
        if request.user.status > 1:
            return simple_response(403)
        data = request.POST
        validate_email(data["email"])
        temp = Temp_user(status=data["status"], email=data["email"], refer=request.user)
        pin = temp.set_pin()
        temp.save()
        return simple_response(201, data={"status": "ok", "pin": pin})
    except KeyError:
        return simple_response(400)
    except ValidationError:
        return simple_response(400)


def edit_user(request):
    data = request.POST
    try:
        if data["action"] == "confirm":
            key = request.session.get("key", False)
            if not key:
                return simple_response(403)
            temp = Temp_user.objects.get(key=key)
            temp.create(data)
        elif data["action"] == "update":
            request.user.update(data)
        elif data["action"] == "reset":
            pass
        elif data["action"] == "change":
            upd_user = User.objects.get(id=data["id"])
            if request.user.status <= upd_user.status and request.user.status <= 1:
                return simple_response(403)
            validate_email(data["email"])
            upd_user.email = data["email"]
            upd_user.save()
            return simple_response(200)
    except KeyError:
        return simple_response(400)
    except ObjectDoesNotExist:
        return simple_response(404)
    except IntegrityError:
        return simple_response(422)
    except ValidationError:
        return simple_response(400)


def get_user(request):
    try:
        data = request.GET
        if data.get("action", False) == "form":
            pin = data["pin"].encode()
            key = data["key"]
            temp = Temp_user.objects.get(key=key)
            if temp.check(pin):
                request.session["temp_id"] = temp.id
                return simple_response(200)
            else:
                return simple_response(400)
        else:
            user = User.objects.get(id=data["id"])
            return simple_response(200, data=user.info(request.user.status))
    except KeyError:
        return simple_response(400)
    except ObjectDoesNotExist:
        return simple_response(404)
    except IntegrityError:
        return simple_response(422)
    except ValidationError:
        return simple_response(400)

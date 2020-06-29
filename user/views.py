from utils import simple_response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from user.models import User


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
    if request.user.id == -1:
        return simple_response(401)
    else:
        return simple_response(200)
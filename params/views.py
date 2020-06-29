from django.core.exceptions import ObjectDoesNotExist
from utils import simple_response
from params.models import Settings, Storage


def settings(request):
    data = request.POST or request.GET
    if request.method == "POST":
        if request.user.status > 2:
            return simple_response(403)
        try:
            key = data["key"].lower()
            value = data["value"]
            access = data.get("access", 5)
            if len(key) > 32 or len(value) > 64 or not all([i in "abcdefghijklmnopqrstuvwxyz_"for i in key]):
                raise KeyError
        except KeyError:
            return simple_response(400)
        try:
            Settings.objects.get(key=key)
            return simple_response(422)
        except ObjectDoesNotExist:
            Settings(key=key, value=value, access=access).save()
            return simple_response(201)
    elif request.method == "GET":
        try:
            key = data["key"].lower()
            s = Settings.objects.get(key=key)
            if request.user.status <= s.access:
                return simple_response(data={key: s.value})
            else:
                return simple_response(403)
        except KeyError:
            return simple_response(400)
        except ObjectDoesNotExist:
            return simple_response(404)
    elif request.method == "PUT":
        if request.user.status > 2:
            return simple_response(403)
        try:
            key = data["key"].lower()
            value = data["value"]
            if len(key) > 32 or len(value) > 64 or not all([i in "abcdefghijklmnopqrstuvwxyz_"for i in key]):
                raise KeyError
        except KeyError:
            return simple_response(400)
        try:
            s = Settings.objects.get(key=key)
            s.change_value(value)
            return simple_response(200)
        except ObjectDoesNotExist:
            return simple_response(422)
    elif request.method == "DELETE":
        if request.user.status > 2:
            return simple_response(403)
        try:
            key = data["key"].lower()
            Settings.objects.get(key=key).delete()
            return simple_response(200)
        except KeyError:
            return simple_response(400)
        except ObjectDoesNotExist:
            return simple_response(404)


def storage(request):
    data = request.POST or request.GET
    if request.method == "POST":
        if request.user.status > 2:
            return simple_response(403)
        try:
            key = data["key"].lower()
            value = data["value"]
            access = data.get("access", 5)
            if len(key) > 32 or not all([i in "abcdefghijklmnopqrstuvwxyz_"for i in key]):
                raise KeyError
        except KeyError:
            return simple_response(400)
        try:
            Storage.objects.get(key=key)
            return simple_response(422)
        except ObjectDoesNotExist:
            Storage(key=key, value=value, access=access).save()
            return simple_response(201)
    elif request.method == "GET":
        try:
            key = data["key"].lower()
            s = Storage.objects.get(key=key)
            if request.user.status <= s.access:
                return simple_response(data={key: s.value})
            else:
                return simple_response(403)
        except KeyError:
            return simple_response(400)
        except ObjectDoesNotExist:
            return simple_response(404)
    elif request.method == "PUT":
        if request.user.status > 2:
            return simple_response(403)
        try:
            key = data["key"].lower()
            value = data["value"]
            if len(key) > 32 or not all([i in "abcdefghijklmnopqrstuvwxyz_"for i in key]):
                raise KeyError
        except KeyError:
            return simple_response(400)
        try:
            s = Storage.objects.get(key=key)
            s.change_value(value)
            return simple_response(200)
        except ObjectDoesNotExist:
            return simple_response(422)
    elif request.method == "DELETE":
        if request.user.status > 2:
            return simple_response(403)
        try:
            key = data["key"].lower()
            Storage.objects.get(key=key).delete()
            return simple_response(200)
        except KeyError:
            return simple_response(400)
        except ObjectDoesNotExist:
            return simple_response(404)
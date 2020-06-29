from django.http import JsonResponse
from media.models import UploadUrl
from django.core.exceptions import ObjectDoesNotExist
from utils import simple_response
from media.models import File, Wallpaper, Image, Skin


def upload(request, **kwargs):
    if request.method != "POST":
        return simple_response(405)
    try:
        key = kwargs["key"]
        uploader = UploadUrl.objects.get(key=key, user=request.user)
        file = request.FILES["file"]
        return simple_response(201, {"status": "ok", "file_name": uploader.upload(file)})
    except KeyError:
        return simple_response(400)
    except ObjectDoesNotExist:
        return simple_response(404)
    except ZeroDivisionError:
        return simple_response(400, data={"status": "File is too large", "code": 7})
    except InterruptedError:
        return simple_response(400, data={"status": "Incorrect width / height ratio", "code": 8})


def delete(request):
    if request.method != "DELETE":
        return simple_response(405)
    try:
        data = request.POST
        name = data["name"]
        type_ = data["type"]
        if request.user.status > 2:
            return simple_response(403)
        if type_ == "file":
            File.objects.get(hash=name).delete_file()
        elif type_ == "image":
            Image.objects.get(hash=name).delete_file()
        elif type_ == "skin":
            Skin.objects.get(hash=name).delete_file()
        elif type_ == "wallpaper":
            Wallpaper.objects.get(hash=name).delete_file()
        return simple_response(200)
    except KeyError:
        return simple_response(400)
    except ObjectDoesNotExist:
        return simple_response(404)


def get_upload_url(request):
    if request.method != "GET":
        return simple_response(405)
    data = request.GET
    if request.user.status <= 2:
        try:
            type_ = data["type"].lower()
            if type_ not in ["image", "file", "skin", "wallpaper"]:
                raise KeyError
            upl = UploadUrl(user=request.user, type=type_)
            if data.get("to", False):
                upl.to = int(data["to"])
            key = upl.set_access()
            upl.save()
            return JsonResponse({"status": "ok", "key": key})
        except KeyError:
            return simple_response(400)
        except ValueError:
            return simple_response(400)
    else:
        return simple_response(403)

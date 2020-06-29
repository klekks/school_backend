from django.http import JsonResponse, HttpResponse
from media.models import UploadUrl
from django.core.exceptions import ObjectDoesNotExist
from utils import simple_response


def upload_image(request, **kwargs):
    if request.method != "POST":
        return simple_response(405)
    try:
        data = request.POST
        key = kwargs["key"]
        uploader = UploadUrl.objects.get(key=key, user=request.user)
        image = request.FILES["image"]
        return HttpResponse(dir(image))
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
            type = data["type"].lower()
            if type not in ["image", "file", "skin", "wallpaper"]:
                raise KeyError
            upl = UploadUrl(user=request.user, type=type)
            key = upl.set_access()
            return JsonResponse({"status": "ok", "key": key})
        except KeyError:
            return simple_response(400)
    else:
        return simple_response(403)

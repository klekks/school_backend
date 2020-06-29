from django.http import JsonResponse, HttpResponse


def upload_image(request):
    print(request.user.id)
    return HttpResponse("sometext")
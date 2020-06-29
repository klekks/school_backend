from random import randint
from django.http import JsonResponse


def hash(length=16):
    s = ''
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(length):
        s += alph[randint(0, len(alph) - 1)]


def simple_response(code=200, data=False):
    if not data:
        response = JsonResponse(response_templates[code])
        response.status_code = code
        return response
    else:
        return JsonResponse(data)


response_templates = {
    200: {"status": "ok"},
    201: {"status": "ok"},
    400: {"status": "One of the parameters was missing or invalid", "code": 2},
    401: {"status": "Unauthorized", "code": 1},
    403: {"status": "Unauthorized", "code": 1},
    404: {"status": "Does not exist", "code": 4},
    405: {"status": "Method not allowed", "code": 5},
    422: {"status": "Already exist", "code": 3},
}
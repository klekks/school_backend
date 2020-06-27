from django.utils.deprecation import MiddlewareMixin
from user.models import User


class CORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        return response


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.session.get("id", False):
            user = User.objects.get(id=request.session["id"])
            request.user = user
        else:
            request.user = User(status=5, id=-1)
        return None

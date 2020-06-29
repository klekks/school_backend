from django.conf.urls import url
from media.views import get_upload_url, upload_image


urlpatterns = [
    url("upload_url", get_upload_url),
    url(r"^upload/(?P<key>[a-zA-Z]{16})/*$", upload_image)
]
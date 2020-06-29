from django.conf.urls import url, re_path
from media.views import get_upload_url, upload, delete


urlpatterns = [
    url("upload_url", get_upload_url),
    url("delete", delete),
    re_path(r"upload/(?P<key>[a-zA-Z]{16})", upload)
]

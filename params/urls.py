from django.conf.urls import url
from params.views import settings, storage

urlpatterns = [
    url("settings", settings),
    url("storage", storage)
]
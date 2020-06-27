"""
Definition of urls for school_backend.
"""

from django.conf.urls import include, url
from media.views import upload_image
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
   url('upload', upload_image),
]

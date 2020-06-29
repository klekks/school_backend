"""
Definition of urls for school_backend.
"""

from django.conf.urls import include, url
from media.views import upload_image


urlpatterns = [
   url('core', include('params.urls')),
   url('user', include('user.urls')),
   url('media', include('media.urls')),
]

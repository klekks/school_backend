"""
Definition of urls for school_backend.
"""

from django.conf.urls import include, url


urlpatterns = [
   url('core', include('params.urls')),
   url('user', include('user.urls')),
   url('media', include('media.urls')),
   url('silk/', include('silk.urls', namespace='silk'))
]

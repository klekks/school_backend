from django.conf.urls import url
from user.views import login, check, user_main

urlpatterns = [
    url("login", login),
    url("check", check),
    url("", user_main)
]
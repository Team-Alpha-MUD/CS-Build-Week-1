from django.conf.urls import url
from django.urls import path, include
from . import api, views

app_name = "adventure"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('rooms', api.rooms)
]

from django.conf.urls import url
from . import api
from django.urls import path, include

from rest_framework import routers
from adventure.api import PlayerViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    path('', include(router.urls)),
]
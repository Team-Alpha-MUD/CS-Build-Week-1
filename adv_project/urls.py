from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

# The next six lines added on model of "Add Routes" in Intro-Django 3
from rest_framework import routers
from adventure.api import PlayerViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('api/', include(router.urls)), # added this line a la Intro-Django 3
]

# we could add path('', include('rest_auth.registration.urls'))
# to make the registration page the homepage
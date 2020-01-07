from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from rest_framework import routers #added
from notes.api import PersonalNoteViewSet #added
from rest_framework.authtoken import views #added

router = routers.DefaultRouter() #added
router.register('notes', PersonalNoteViewSet) #added

urlpatterns = [
    path('', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
]

from django.contrib import admin
from adventure.models import Player, Room
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
admin.site.register(Player)
admin.site.register(Room)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room, Player
from util.world_map import world

# Create your views here.
def homepage(request):
    # return HttpResponse("This is created by <strong>Django</strong>!")
    return render(request=request, 
                  template_name='adventure/home.html',
                  context={'room': Room.objects.all,
                           'player': Player.objects.all,
                           'world': world})

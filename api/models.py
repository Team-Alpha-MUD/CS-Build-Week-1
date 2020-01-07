from django.db import models

# Create your models here.
from rest_framework import serializers, viewsets #added
from adventure.models import Player #added

class PlayerSerializer(serializers.HyperlinkedModelSerializer): #added

    class Meta: #added
        model = Player #added
        fields = ('user', 'currentRoom') #added

    def create(self, validated_data): #added
        #import pdb; pdb.set_trace()
        user = self.context['request'].user #added
        player = Player.objects.create(user=user, **validated_data) #added
        return player #added

class PlayerViewSet(viewsets.ModelViewSet): #added
    serializer_class = PlayerSerializer #added
    queryset = Player.objects.none() #added

    def get_queryset(self): #added
        user = self.request.user #added
        if user.is_anonymous: #added
            return Player.objects.none() #added
        else: #added
            return Player.objects.filter(user=user) #added


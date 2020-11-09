from rest_framework import viewsets

from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

from homepage.models import Games
from homepage.serializer import GameSerializer


## API
class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GameSerializer

## INDEX
def index(request): 
    games = Games.objects.all()
    return render(request, "homepage/index.html", { 'games' : games})

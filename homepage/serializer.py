from rest_framework import serializers
from homepage.models import Games

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', 'titulo', 'plataformas']

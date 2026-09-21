from rest_framework import serializers
from .models import Genero, Plataforma, Videojuego


class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = '__all__'


class PlataformaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plataforma
        fields = '__all__'


class VideojuegoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Videojuego
        fields = '__all__'
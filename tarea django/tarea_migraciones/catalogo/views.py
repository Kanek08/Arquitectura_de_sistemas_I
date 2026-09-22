from rest_framework import viewsets
from .models import Genero, Plataforma, Videojuego
from .serializers import (
    GeneroSerializer,
    PlataformaSerializer,
    VideojuegoSerializer
)


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objetos.all()
    serializer_class = GeneroSerializer


class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objetos.all()
    serializer_class = PlataformaSerializer


class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objetos.all()
    serializer_class = VideojuegoSerializer

from rest_framework import viewsets

from .models import Comentario, Resena, VotoUtil
from .serializers import ComentarioSerializer, ResenaSerializer, VotoUtilSerializer


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objetos.all()
    serializer_class = ResenaSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objetos.all()
    serializer_class = ComentarioSerializer


class VotoUtilViewSet(viewsets.ModelViewSet):
    queryset = VotoUtil.objetos.all()
    serializer_class = VotoUtilSerializer

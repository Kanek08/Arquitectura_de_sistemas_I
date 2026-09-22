from rest_framework import viewsets
from .models import DireccionEnvio, Rol, Usuario
from .serializers import DireccionEnvioSerializer, RolSerializer, UsuarioSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objetos.all()
    serializer_class = RolSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objetos.all()
    serializer_class = UsuarioSerializer


class DireccionEnvioViewSet(viewsets.ModelViewSet):
    queryset = DireccionEnvio.objetos.all()
    serializer_class = DireccionEnvioSerializer


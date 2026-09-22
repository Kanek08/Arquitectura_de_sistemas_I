from rest_framework import serializers
from .models import DireccionEnvio, Rol, Usuario


class RolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'


class DireccionEnvioSerializer(serializers.ModelSerializer):

    class Meta:
        model = DireccionEnvio
        fields = '__all__'

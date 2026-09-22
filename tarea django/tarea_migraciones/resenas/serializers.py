from rest_framework import serializers

from .models import Comentario, Resena, VotoUtil


class ResenaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resena
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = '__all__'


class VotoUtilSerializer(serializers.ModelSerializer):

    class Meta:
        model = VotoUtil
        fields = '__all__'

from rest_framework import serializers

from .models import Almacen, Proveedor, Stock


class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = '__all__'


class AlmacenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Almacen
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'

from rest_framework import serializers

from .models import DetallePedido, Pago, Pedido


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ('fecha_pedido',)


class DetallePedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetallePedido
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pago
        fields = '__all__'

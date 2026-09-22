from rest_framework import viewsets

from .models import DetallePedido, Pago, Pedido
from .serializers import DetallePedidoSerializer, PagoSerializer, PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objetos.all()
    serializer_class = PedidoSerializer


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objetos.all()
    serializer_class = DetallePedidoSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objetos.all()
    serializer_class = PagoSerializer

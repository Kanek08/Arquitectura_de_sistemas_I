from rest_framework import viewsets

from .models import Almacen, Proveedor, Stock
from .serializers import AlmacenSerializer, ProveedorSerializer, StockSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objetos.all()
    serializer_class = ProveedorSerializer


class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objetos.all()
    serializer_class = AlmacenSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objetos.all()
    serializer_class = StockSerializer

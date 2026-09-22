from django.db import models
from core.models import ModeloBase
from catalogo.models import Videojuego


class Proveedor(ModeloBase):
    nombre = models.CharField(max_length=150)
    contacto_email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    calificacion = models.FloatField(
        default=0.0,
        help_text='Calificación del proveedor de 0.0 a 5.0'
    )
    esta_habilitado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['-calificacion']

    def __str__(self):
        return self.nombre


class Almacen(ModeloBase):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200)
    capacidad_maxima = models.PositiveIntegerField(
        help_text='Cantidad máxima de unidades que puede almacenar'
    )
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    stock_minimo = models.PositiveIntegerField(  # ← NUEVO CAMPO
        default=10,
        help_text='Cantidad mínima antes de alertar reabastecimiento'
    )

    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Stock(ModeloBase):
    videojuego = models.ForeignKey(
        Videojuego,
        on_delete=models.CASCADE,
        related_name='registros_stock'
    )
    almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE,
        related_name='registros_stock'
    )
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        related_name='registros_stock'
    )
    cantidad_disponible = models.PositiveIntegerField(default=0)
    ultima_entrada = models.DateField(
        help_text='Fecha del último reabastecimiento'
    )

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'
        ordering = ['-ultima_entrada']
        unique_together = ('videojuego', 'almacen')

    def __str__(self):
        return f'{self.videojuego} en {self.almacen}: {self.cantidad_disponible}'
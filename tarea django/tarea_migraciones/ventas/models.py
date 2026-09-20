from django.db import models
from core.models import ModeloBase
from usuarios.models import Usuario
from catalogo.models import Videojuego


class Pedido(ModeloBase):
    class Estado(models.TextChoices):
        PENDIENTE = 'PE', 'Pendiente'
        PAGADO = 'PA', 'Pagado'
        ENVIADO = 'EN', 'Enviado'
        CANCELADO = 'CA', 'Cancelado'

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='pedidos'
    )
    fecha_pedido = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notas = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha_pedido']

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario}'


class DetallePedido(ModeloBase):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    videojuego = models.ForeignKey(
        Videojuego,
        on_delete=models.PROTECT,
        related_name='detalles_pedido'
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='Precio del juego al momento de la compra'
    )

    class Meta:
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalles de pedido'
        unique_together = ('pedido', 'videojuego')

    def __str__(self):
        return f'{self.cantidad}x {self.videojuego} en {self.pedido}'

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario


class Pago(ModeloBase):
    class MetodoPago(models.TextChoices):
        TARJETA = 'TA', 'Tarjeta'
        TRANSFERENCIA = 'TR', 'Transferencia'
        EFECTIVO = 'EF', 'Efectivo'

    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE,
        related_name='pago'
    )
    metodo = models.CharField(max_length=2, choices=MetodoPago.choices)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fue_exitoso = models.BooleanField(default=False)
    fecha_pago = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-fecha_pago']

    def __str__(self):
        return f'Pago de {self.pedido}'
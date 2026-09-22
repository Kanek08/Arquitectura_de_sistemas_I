from django.contrib import admin
from .models import Pedido, DetallePedido, Pago


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'estado', 'total', 'fecha_pedido')
    list_filter = ('estado',)
    search_fields = ('usuario__nombre_completo',)
    inlines = [DetallePedidoInline]


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'metodo', 'monto', 'fue_exitoso', 'fecha_pago')
    list_filter = ('metodo', 'fue_exitoso')
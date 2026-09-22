from django.contrib import admin
from .models import Proveedor, Almacen, Stock


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calificacion', 'esta_habilitado')
    search_fields = ('nombre',)


@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'capacidad_maxima')
    search_fields = ('nombre',)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('videojuego', 'almacen', 'proveedor', 'cantidad_disponible', 'ultima_entrada')
    list_filter = ('almacen', 'proveedor')
    search_fields = ('videojuego__nombre',)
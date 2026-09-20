from django.contrib import admin
from .models import Genero, Plataforma, Videojuego


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'esta_activo', 'fecha_creacion')
    search_fields = ('nombre',)


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fabricante', 'es_portatil', 'esta_activo')
    search_fields = ('nombre', 'fabricante')


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'precio', 'disponible', 'fecha_lanzamiento')
    list_filter = ('genero', 'plataformas', 'clasificacion', 'multijugador')
    search_fields = ('nombre',)
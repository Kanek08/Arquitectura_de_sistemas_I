from django.contrib import admin
from .models import Resena, Comentario, VotoUtil


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'videojuego', 'usuario', 'calificacion', 'recomendado')
    list_filter = ('calificacion', 'recomendado')
    search_fields = ('titulo', 'videojuego__nombre')
    inlines = [ComentarioInline]


@admin.register(VotoUtil)
class VotoUtilAdmin(admin.ModelAdmin):
    list_display = ('resena', 'usuario', 'es_util')
    list_filter = ('es_util',)
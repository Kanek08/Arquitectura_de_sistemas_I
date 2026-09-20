from django.contrib import admin
from .models import Rol, Usuario, DireccionEnvio


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel_acceso', 'esta_activo')
    search_fields = ('nombre',)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'email', 'rol', 'esta_verificado')
    list_filter = ('rol', 'esta_verificado')
    search_fields = ('nombre_completo', 'email')


@admin.register(DireccionEnvio)
class DireccionEnvioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calle', 'ciudad', 'es_predeterminada')
    list_filter = ('ciudad', 'es_predeterminada')
    search_fields = ('usuario__nombre_completo', 'calle')
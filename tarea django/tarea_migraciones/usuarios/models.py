from django.db import models
from core.models import ModeloBase


class Rol(ModeloBase):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    nivel_acceso = models.PositiveIntegerField(
        default=1,
        help_text='Nivel numérico de permisos (mayor número = más acceso)'
    )

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nivel_acceso']

    def __str__(self):
        return self.nombre


class Usuario(ModeloBase):
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    esta_verificado = models.BooleanField(default=False)

    rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        related_name='usuarios'
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre_completo']

    def __str__(self):
        return self.nombre_completo


class DireccionEnvio(ModeloBase):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='direcciones'
    )
    calle = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    es_predeterminada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Dirección de envío'
        verbose_name_plural = 'Direcciones de envío'
        ordering = ['-es_predeterminada']

    def __str__(self):
        return f'{self.calle}, {self.ciudad}'
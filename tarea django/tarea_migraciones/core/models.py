import uuid
from django.db import models
from django.utils import timezone


class GestorActivos(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esta_activo=True)


class ModeloBase(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='ID'
    )
    esta_activo = models.BooleanField(
        default=True,
        verbose_name='Activo',
        help_text='Indica si el registro está activo (soft delete)'
    )
    fecha_eliminacion = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Fecha de eliminación'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de modificación'
    )

    objetos = GestorActivos()          # solo activos (uso por defecto)
    todos_los_objetos = models.Manager()  # incluye eliminados

    class Meta:
        abstract = True
        ordering = ['-fecha_creacion']

    def eliminar_logico(self):
        """Realiza un soft delete: marca el registro como inactivo."""
        self.esta_activo = False
        self.fecha_eliminacion = timezone.now()
        self.save(update_fields=['esta_activo', 'fecha_eliminacion'])

    def restaurar(self):
        """Revierte un soft delete."""
        self.esta_activo = True
        self.fecha_eliminacion = None
        self.save(update_fields=['esta_activo', 'fecha_eliminacion'])
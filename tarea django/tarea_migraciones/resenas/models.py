from django.db import models
from core.models import ModeloBase
from usuarios.models import Usuario
from catalogo.models import Videojuego


class Resena(ModeloBase):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    videojuego = models.ForeignKey(
        Videojuego,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    calificacion = models.PositiveIntegerField(
        help_text='Calificación de 1 a 5'
    )
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    recomendado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
        ordering = ['-fecha_creacion']
        unique_together = ('usuario', 'videojuego')

    def __str__(self):
        return f'{self.titulo} ({self.videojuego})'


class Comentario(ModeloBase):
    resena = models.ForeignKey(
        Resena,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    contenido = models.TextField()
    fecha_edicion = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'Comentario de {self.usuario} en {self.resena}'


class VotoUtil(ModeloBase):
    resena = models.ForeignKey(
        Resena,
        on_delete=models.CASCADE,
        related_name='votos'
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='votos_utiles'
    )
    es_util = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Voto útil'
        verbose_name_plural = 'Votos útiles'
        unique_together = ('resena', 'usuario')

    def __str__(self):
        return f'{self.usuario} votó en {self.resena}'
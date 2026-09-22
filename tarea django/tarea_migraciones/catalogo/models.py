from django.db import models
from core.models import ModeloBase


class Genero(ModeloBase):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Plataforma(ModeloBase):
    nombre = models.CharField(max_length=50, unique=True)
    fabricante = models.CharField(max_length=100)
    es_portatil = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Videojuego(ModeloBase):
    class Clasificacion(models.TextChoices):
        TODOS = 'E', 'Para todos'
        ADOLESCENTES = 'T', 'Adolescentes'
        MADURO = 'M', 'Maduro'
        ADULTOS = 'AO', 'Solo adultos'

    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField(blank=True)
    clasificacion = models.CharField(
        max_length=2,
        choices=Clasificacion.choices,
        default=Clasificacion.TODOS
    )
    disponible = models.BooleanField(default=True)
    cantidad_jugadores_local = models.PositiveIntegerField(default=1)
    multijugador = models.BooleanField(default=False)
    fecha_lanzamiento = models.DateField()

    genero = models.ForeignKey(
        Genero,
        on_delete=models.PROTECT,
        related_name='videojuegos'
    )
    plataformas = models.ManyToManyField(
        Plataforma,
        related_name='videojuegos'
    )

    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
from rest_framework.routers import DefaultRouter

from .views import GeneroViewSet, PlataformaViewSet, VideojuegoViewSet


router = DefaultRouter()
router.register('generos', GeneroViewSet)
router.register('plataformas', PlataformaViewSet)
router.register('videojuegos', VideojuegoViewSet)

urlpatterns = router.urls

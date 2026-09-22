from rest_framework.routers import DefaultRouter

from .views import ComentarioViewSet, ResenaViewSet, VotoUtilViewSet


router = DefaultRouter()
router.register('resenas', ResenaViewSet)
router.register('comentarios', ComentarioViewSet)
router.register('votos-utiles', VotoUtilViewSet)

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import DireccionEnvioViewSet, RolViewSet, UsuarioViewSet


router = DefaultRouter()

router.register('roles', RolViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('direcciones', DireccionEnvioViewSet)

urlpatterns = router.urls

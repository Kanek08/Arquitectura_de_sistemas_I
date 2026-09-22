from rest_framework.routers import DefaultRouter

from .views import DetallePedidoViewSet, PagoViewSet, PedidoViewSet


router = DefaultRouter()
router.register('pedidos', PedidoViewSet)
router.register('detalles-pedido', DetallePedidoViewSet)
router.register('pagos', PagoViewSet)

urlpatterns = router.urls

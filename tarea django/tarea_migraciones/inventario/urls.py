from rest_framework.routers import DefaultRouter

from .views import AlmacenViewSet, ProveedorViewSet, StockViewSet


router = DefaultRouter()
router.register('proveedores', ProveedorViewSet)
router.register('almacenes', AlmacenViewSet)
router.register('stock', StockViewSet)

urlpatterns = router.urls

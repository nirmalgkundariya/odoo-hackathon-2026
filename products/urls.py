from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductVariantViewSet

router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('variants', ProductVariantViewSet)

urlpatterns = router.urls
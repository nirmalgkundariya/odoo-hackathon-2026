from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceLineViewSet

router = DefaultRouter()

router.register('invoices', InvoiceViewSet)
router.register('invoice-lines', InvoiceLineViewSet)

urlpatterns = router.urls
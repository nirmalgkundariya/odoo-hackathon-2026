from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, SubscriptionLineViewSet

router = DefaultRouter()

router.register('subscriptions', SubscriptionViewSet)
router.register('subscription-lines', SubscriptionLineViewSet)

urlpatterns = router.urls
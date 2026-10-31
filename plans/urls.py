from rest_framework.routers import DefaultRouter
from .views import PlanViewSet

router = DefaultRouter()

router.register('plans', PlanViewSet)

urlpatterns = router.urls
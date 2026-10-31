from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Plan
from .serializers import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):

    queryset = Plan.objects.prefetch_related('products').all().order_by('-id')

    serializer_class = PlanSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
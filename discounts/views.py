from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Discount
from .serializers import DiscountSerializer


class DiscountViewSet(viewsets.ModelViewSet):

    queryset = Discount.objects.prefetch_related(
        'products'
    ).all().order_by('-id')

    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated]
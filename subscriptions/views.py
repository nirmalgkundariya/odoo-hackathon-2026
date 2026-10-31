from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Subscription, SubscriptionLine
from .serializers import (
    SubscriptionSerializer,
    SubscriptionLineSerializer
)


class SubscriptionViewSet(viewsets.ModelViewSet):

    queryset = Subscription.objects.select_related(
        'customer', 'plan'
    ).all().order_by('-id')

    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionLineViewSet(viewsets.ModelViewSet):

    queryset = SubscriptionLine.objects.select_related(
        'subscription', 'product', 'variant'
    ).all()

    serializer_class = SubscriptionLineSerializer
    permission_classes = [IsAuthenticated]
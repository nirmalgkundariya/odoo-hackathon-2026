from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.select_related(
        'invoice'
    ).all().order_by('-id')

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
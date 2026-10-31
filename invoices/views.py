from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Invoice, InvoiceLine
from .serializers import InvoiceSerializer, InvoiceLineSerializer


class InvoiceViewSet(viewsets.ModelViewSet):

    queryset = Invoice.objects.select_related(
        'subscription'
    ).all().order_by('-id')

    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]


class InvoiceLineViewSet(viewsets.ModelViewSet):

    queryset = InvoiceLine.objects.select_related('invoice').all()

    serializer_class = InvoiceLineSerializer
    permission_classes = [IsAuthenticated]
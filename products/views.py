from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductVariantViewSet(viewsets.ModelViewSet):

    queryset = ProductVariant.objects.select_related('product').all()
    serializer_class = ProductVariantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
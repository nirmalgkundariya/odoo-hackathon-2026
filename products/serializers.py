from rest_framework import serializers
from .models import Product, ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):

    final_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = '__all__'

    def get_final_price(self, obj):
        return obj.get_price()


class ProductSerializer(serializers.ModelSerializer):

    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
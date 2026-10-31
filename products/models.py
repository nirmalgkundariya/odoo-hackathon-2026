from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=100)

    sales_price = models.DecimalField(
        max_digits=12, decimal_places=2
    )

    cost_price = models.DecimalField(
        max_digits=12, decimal_places=2
    )

    notes = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )

    brand = models.CharField(max_length=100)

    price_adjustment = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def get_price(self):
        return self.product.sales_price + self.price_adjustment

    def __str__(self):
        return f"{self.product.name} - {self.brand}"
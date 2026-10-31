from django.db import models
from products.models import Product


class Discount(models.Model):

    TYPE_CHOICES = [
        ('FIXED', 'Fixed Amount'),
        ('PERCENTAGE', 'Percentage'),
    ]

    name = models.CharField(max_length=150)

    discount_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    value = models.DecimalField(
        max_digits=10, decimal_places=2
    )

    minimum_purchase = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )

    minimum_quantity = models.PositiveIntegerField(default=1)

    products = models.ManyToManyField(Product, blank=True)

    apply_to_subscription = models.BooleanField(default=False)

    start_date = models.DateField()
    end_date = models.DateField()

    usage_limit = models.PositiveIntegerField(default=0)
    usage_count = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
from django.db import models
from products.models import Product


class Plan(models.Model):

    BILLING_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
    ]

    name = models.CharField(max_length=200)

    products = models.ManyToManyField(Product)

    price = models.DecimalField(
        max_digits=12, decimal_places=2
    )

    billing_cycle = models.CharField(
        max_length=20,
        choices=BILLING_CHOICES
    )

    minimum_quantity = models.PositiveIntegerField(default=1)

    available_from = models.DateField()
    available_until = models.DateField(null=True, blank=True)

    auto_close = models.BooleanField(default=False)
    allow_pause = models.BooleanField(default=True)
    allow_early_close = models.BooleanField(default=True)
    allow_renewal = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
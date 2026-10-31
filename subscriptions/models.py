from django.db import models
from django.contrib.auth.models import User
from plans.models import Plan
from products.models import Product, ProductVariant


class Subscription(models.Model):

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('QUOTATION', 'Quotation'),
        ('CONFIRMED', 'Confirmed'),
        ('ACTIVE', 'Active'),
        ('PAUSED', 'Paused'),
        ('CLOSED', 'Closed'),
    ]

    subscription_number = models.CharField(
        max_length=30, unique=True
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='subscriptions'
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT
    )

    start_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )

    payment_terms = models.CharField(
        max_length=100,
        default='Due on receipt'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subscription_number


class SubscriptionLine(models.Model):

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        related_name='lines'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(
        max_digits=12, decimal_places=2
    )

    tax_rate = models.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )

    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    @property
    def total(self):
        return self.subtotal * (1 + self.tax_rate / 100)
from django.db import models
from subscriptions.models import Subscription


class Invoice(models.Model):

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('CONFIRMED', 'Confirmed'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled'),
    ]

    invoice_number = models.CharField(
        max_length=30, unique=True
    )

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.PROTECT,
        related_name='invoices'
    )

    billing_period_start = models.DateField()
    billing_period_end = models.DateField()
    due_date = models.DateField()

    subtotal = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )

    tax_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )

    discount_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )

    total_amount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'subscription',
                    'billing_period_start',
                    'billing_period_end'
                ],
                name='unique_subscription_billing_period'
            )
        ]

    def __str__(self):
        return self.invoice_number


class InvoiceLine(models.Model):

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name='lines'
    )

    description = models.CharField(max_length=200)

    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(
        max_digits=12, decimal_places=2
    )

    tax_rate = models.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )

    def __str__(self):
        return self.description
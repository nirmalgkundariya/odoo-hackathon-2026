from django.db import models
from invoices.models import Invoice


class Payment(models.Model):

    METHOD_CHOICES = [
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
        ('UPI', 'UPI'),
        ('BANK', 'Bank Transfer'),
        ('ONLINE', 'Online'),
    ]

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.PROTECT,
        related_name='payments'
    )

    method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES
    )

    amount = models.DecimalField(
        max_digits=12, decimal_places=2
    )

    payment_date = models.DateField()

    note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.amount}"
from datetime import date
from decimal import Decimal

from django.db.models import Sum, Count, F, DecimalField, ExpressionWrapper
from django.db.models.functions import Coalesce

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from subscriptions.models import Subscription
from invoices.models import Invoice
from payments.models import Payment


class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        today = date.today()

        active_subscriptions = Subscription.objects.filter(
            status='ACTIVE'
        ).count()

        total_customers = Subscription.objects.values(
            'customer'
        ).distinct().count()

        total_revenue = Payment.objects.aggregate(
            total=Coalesce(
                Sum('amount'),
                Decimal('0.00')
            )
        )['total']

        invoice_data = Invoice.objects.exclude(
            status='CANCELLED'
        ).annotate(
            paid_amount=Coalesce(
                Sum('payments__amount'),
                Decimal('0.00'),
                output_field=DecimalField(max_digits=14, decimal_places=2)
            )
        )

        total_outstanding = Decimal('0.00')

        for invoice in invoice_data:
            balance = invoice.total_amount - invoice.paid_amount
            total_outstanding += max(balance, Decimal('0.00'))

        overdue_invoices = Invoice.objects.filter(
            due_date__lt=today
        ).exclude(
            status__in=['PAID', 'CANCELLED']
        ).count()

        recent_payments = Payment.objects.select_related(
            'invoice'
        ).order_by('-created_at')[:5]

        recent_data = [
            {
                'invoice': p.invoice.invoice_number,
                'amount': str(p.amount),
                'method': p.method,
                'date': str(p.payment_date),
            }
            for p in recent_payments
        ]

        return Response({
            'active_subscriptions': active_subscriptions,
            'total_customers': total_customers,
            'total_revenue': str(total_revenue),
            'total_outstanding': str(total_outstanding),
            'overdue_invoices': overdue_invoices,
            'recent_payments': recent_data,
        })
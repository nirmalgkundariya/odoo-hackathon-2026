from rest_framework import serializers
from .models import Subscription, SubscriptionLine


class SubscriptionLineSerializer(serializers.ModelSerializer):

    subtotal = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

    class Meta:
        model = SubscriptionLine
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    lines = SubscriptionLineSerializer(many=True, read_only=True)
    customer_name = serializers.CharField(
        source='customer.username',
        read_only=True
    )
    plan_name = serializers.CharField(
        source='plan.name',
        read_only=True
    )

    class Meta:
        model = Subscription
        fields = '__all__'
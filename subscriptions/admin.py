from django.contrib import admin
from .models import Subscription, SubscriptionLine

admin.site.register(Subscription)
admin.site.register(SubscriptionLine)
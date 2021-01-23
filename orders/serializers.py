from rest_framework.serializers import ModelSerializer
from orders.models import (
    Issue,
    Tracker,
    Order,
)
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"

class TrackerSerializer(ModelSerializer):

    class Meta:
        model = Tracker
        fields = "__all__"

class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

class OrderDetailsSerializer(ModelSerializer):

    customer_info = serializers.ReadOnlyField(
        source="customer.info"
    )
    product_info = serializers.ReadOnlyField(
        source = "product.info"
    )
    address_info = serializers.ReadOnlyField(
        source = "address.info"
    )
    store_info = serializers.ReadOnlyField(
        source = "store.info"
    )
    tracker_info = serializers.ReadOnlyField(
        source = "tracker.info"
    )

    class Meta:
        model = Order
        fields = (
            "id", "customer_info", "product_info", "address_info",
            "tracker_info", "store_info", "status", "quantity", "issues"
        )

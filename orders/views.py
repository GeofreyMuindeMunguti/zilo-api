from django.shortcuts import render
from orders.serializers import (
    TrackerSerializer,
    OrderSerializer,
    OrderDetailsSerializer,
    IssueSerializer,
)
from orders.models import (
    Tracker,
    Order,
    Issue
)
from rest_framework.viewsets import ModelViewSet

class TrackerViewSet(ModelViewSet):

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer

class IssueViewSet(ModelViewSet):

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderDetailsSerializer
        return OrderSerializer

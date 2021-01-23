from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from inventory.models import (
    Product
)
from inventory.serializers import (
    ProductSerializer
)


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
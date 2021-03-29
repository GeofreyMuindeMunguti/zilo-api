from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import (
    generics,
    permissions
)
from users.serializers import (
    UserSerializer,
    UserRegisterSerializer,
    CompanySerializer,
    CustomerSerializer,
    AddressSerializer,
    StoreSerializer,
)
from users.models import (
    User,
    Company,
    Customer,
    Address,
    Store
)
# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer
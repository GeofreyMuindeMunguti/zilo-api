from users.models import (
    User,
    Company,
    Address,
    Customer,
    Store,
)
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"

class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"

class StoreSerializer(ModelSerializer):

    class Meta:
        model = Store
        fields = "__all__"
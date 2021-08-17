
from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.models import (
    User,
    Company,
    Address,
    Customer,
    Store,
)


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"

class UserRegisterSerializer(ModelSerializer):

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True)

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        return user

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
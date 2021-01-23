import uuid
from django.db import models
from common.models import AbstractBase
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.contrib.auth.models import UserManager
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password

# Create your models here.
class MyUserManager(BaseUserManager):
    """
    Reimplementing the django.contrib.auth.models UserManager
    by extending the BaseUserManager
    """

    def create(self, first_name, email=None, password=None, **extra_fields):
        """Create a normal user."""
        if email:
            validate_email(email)
            email = MyUserManager.normalize_email(email)
        p = make_password(password)
        user = self.model(
            first_name=first_name, email=email, password=p, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, password, **extra_fields):
        """Create a superuser."""
        user = self.create(first_name, 'muinde@zilo.com', password, **extra_fields)
        user.save(using=self._db)
        return user


class Address(AbstractBase):

    name = models.CharField(max_length = 30)
    description = models.TextField(blank = True, null = True)
    latitude = models.DecimalField(decimal_places=10, max_digits=30, blank = True, null = True)
    longitude = models.DecimalField(decimal_places=10, max_digits=30, blank = True, null = True)

    def __str__(self):
        return f"{self.name} - {self.description}"

    @property
    def info(self):
        return {
            "name": self.name,
            "description": self.description,
            "latitude": self.latitude,
            "longitude": self.longitude
        }


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null= True)
    code = models.CharField(
        max_length=254, unique=True,
        null=True, blank=True, default=None
    )

    objects = MyUserManager()

    USERNAME_FIELD = "code"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.code or self.first_name

class Customer(AbstractBase):

    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(blank = True, null = True, max_length=13)
    addresses = models.ManyToManyField(Address, blank = True, related_name = "customer")

    def __str__(self):
        return f"{self.name} - {self.email}"

    @property
    def info(self):

        return {
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }

    class Meta:
        unique_together = ("email", "phone_number", "name")

class Company(AbstractBase):

    name = models.CharField(max_length=30)
    employees = models.ManyToManyField(User, blank = True, related_name = "company")

    def __str__(self):
        return f"{self.name}"
    
    @property
    def info(self):
        return {
            "name": self.name
        }

class Store(AbstractBase):
    
    name = models.CharField(max_length = 30)
    address = models.ForeignKey(Address, related_name = "store", on_delete=models.PROTECT)
    company = models.ForeignKey(Company, related_name = "store", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.company.name}"

    @property
    def info(self):
        return {
            "name": self.name,
            "address": self.address.info,
            "company": self.company.info
        }

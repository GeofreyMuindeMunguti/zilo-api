from django.db import models
from common.models import AbstractBase
from users.models import (
    Company
)
# Create your models here.

class Product(AbstractBase):

    name = models.CharField(max_length = 30)
    description = models.TextField(blank = True, null = True)
    company = models.ForeignKey(Company, related_name = "products", default = "5b881a64-ac3f-43c4-b528-a634f0fe85ab", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.company.name}"

    @property
    def info(self):
        return {
            "name": self.name,
            "company": self.company.name,
            "description": self.description
        }
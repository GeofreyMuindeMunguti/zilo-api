from django.db import models
from common.models import AbstractBase
from users.models import (
    User,
    Customer,
    Company,
    Address,
    Store
)
from inventory.models import (
    Product,
)
# Create your models here.

DELIVERY_STATUSES = (
    ("RECEIVED", "RECEIVED"),
    ("PICKED", "PICKED"),
    ("TRACKING", "TRACKING"),
    ("FULLFILLED", "FULLFILLED")
)
TRACKER_CHOICES = (
    ("ONGOING", "ONGOING"),
    ("DONE", "DONE")
)

class Issue(AbstractBase):

    name = models.CharField(max_length = 30)
    description = models.TextField(blank = True, null = True)
    assignee = models.ForeignKey(User, related_name="issues", on_delete=models.PROTECT)

class Tracker(AbstractBase):

    live_location_lat = models.CharField(max_length = 30)
    live_location_long = models.CharField(max_length = 30)
    status = models.CharField(max_length=30, default="ONGOING", choices = TRACKER_CHOICES)

    def __str__(self):
        return f"{self.status}"
    @property
    def info(self):
        return {
            "live_location_lat": self.live_location_lat,
            "live_location_long": self.live_location_long,
            "status": self.status
        }

class Order(AbstractBase):

    customer = models.ForeignKey(Customer, related_name = "orders", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name = "orders", on_delete=models.PROTECT)
    quantity = models.IntegerField()
    delivery_address = models.ForeignKey(Address, related_name="orders", on_delete=models.PROTECT)
    store = models.ForeignKey(Store, related_name="orders", on_delete = models.PROTECT)
    status = models.CharField(choices = DELIVERY_STATUSES, default="RECEIVED", max_length = 30)
    tracker = models.ForeignKey(Tracker, blank = True, null = True, related_name="orders", on_delete=models.PROTECT)
    issues = models.ManyToManyField(Issue, blank = True, related_name="orders")

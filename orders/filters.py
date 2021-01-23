from common.filters import CommonFieldsFilterset
from orders.models import (
    Order
)

class OrderFilter(CommonFieldsFilterset):

    class Meta:
        model = Order
        fields = ["product"]
        order_by = ["-created_at", "-updated_at"]
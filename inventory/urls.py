from django.urls import include
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from inventory.views import (
    ProductViewSet
)

router = SimpleRouter()

router.register(
    "products",
    ProductViewSet,
    "products"
)

urlpatterns = [
    url("", include(router.urls))
]
from django.urls import include
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from users.views import (
    UserViewSet,
    CompanyViewSet,
    CustomerViewSet,
    AddressViewSet,
    StoreViewSet,
)


router = SimpleRouter()

router.register(
    "users", UserViewSet,
    "users"
)
router.register(
    "companies",
    CompanyViewSet,
    "companies"
)
router.register(
    "customers",
    CustomerViewSet,
    "customers"
)
router.register(
    "addresses",
    AddressViewSet,
    "addresses"
)
router.register(
    "stores",
    StoreViewSet,
    "stores"
)

urlpatterns = [
    url("", include(router.urls)),
]

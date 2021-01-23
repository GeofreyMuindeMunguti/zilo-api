from django.urls import include
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from orders.views import (
    IssueViewSet,
    OrderViewSet,
    TrackerViewSet,
)

router = SimpleRouter()

router.register(
    "issues",
    IssueViewSet,
    "issues"
)
router.register(
    "trackers",
    TrackerViewSet,
    "trackers"
)
router.register(
    "",
    OrderViewSet,
    "orders"
)

urlpatterns = [
    url("", include(router.urls))
]
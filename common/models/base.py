import uuid
from django.utils import timezone
from django.db import models
from django.conf import settings

class AbstractBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(
        default=False,
        help_text="Deletes should deactivate not do actual deletes")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True,
        on_delete=models.PROTECT, related_name="+")

    class Meta(object):
        abstract = True
        ordering = ("-created_at", "-updated_at")
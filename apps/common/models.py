from django.db import models
from django.utils.translation import gettext_lazy as _

PENDING, IN_PROGRESS, COMPLETED, EXPIRED = "pending", "in_progress", "completed", "expired"

TASK_STATUS = (
    (PENDING, PENDING),
    (IN_PROGRESS, IN_PROGRESS),
    (COMPLETED, COMPLETED),
    (EXPIRED, EXPIRED),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    status = models.CharField(
        max_length=255,
        choices=TASK_STATUS,
        default=PENDING,
        verbose_name=_("Status")
    )
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tasks",
        verbose_name=_("User")
    )

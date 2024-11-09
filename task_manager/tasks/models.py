from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    status = models.ForeignKey(
        Status,
        verbose_name=_("Status"),
        on_delete=models.PROTECT
    )
    executor = models.ForeignKey(
        User,
        verbose_name=_("Executor"),
        on_delete=models.PROTECT,
        blank=True, null=True
    )
    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.PROTECT,
        related_name='task_created'
    )
    labels = models.ManyToManyField(
        Label,
        verbose_name=_("Labels"),
        through='TasksRelationLabels',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date of creation")
    )

    def __str__(self):
        return self.name


class TasksRelationLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

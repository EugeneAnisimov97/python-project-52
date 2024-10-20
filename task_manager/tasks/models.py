from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_created') 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
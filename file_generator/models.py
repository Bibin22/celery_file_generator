from django.db import models
import uuid
from django_celery_results.models import TaskResult

class TblCeleryLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    celery_task_id = models.CharField(max_length=100, null=True, blank=True)
    filename = models.CharField(max_length=100, null=True, blank=True)
    data_count = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    status = models.ForeignKey(TaskResult, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.filename

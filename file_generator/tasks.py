from telnetlib import STATUS
from django.shortcuts import render, HttpResponse
from celery import shared_task
import csv
import random
import string
from django.core.files.base import ContentFile
from django_celery_results.models import TaskResult
from .models import *
from celery.result import AsyncResult


@shared_task(bind=True)
def generate_file(self, filename, raw_count):
    task_id = generate_file.request.id
    file_name = str(filename)+".csv"
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = "' + file_name + '"'
    writer = csv.writer(response)
    first_raw = ['Random Data']
    writer.writerow(first_raw)
    for i in range(1, raw_count+1):
        random_raw = [(''.join(random.choices(string.ascii_lowercase, k=5)))]
        writer.writerow(random_raw)
    tasks = TaskResult.objects.get(task_id=task_id)
    csv_file = TblCeleryLog(celery_task_id=task_id, filename=filename, data_count=raw_count, status=tasks)
    csv_file.file.save(file_name, ContentFile(response.content))    

    csv_file.save()

    # result = AsyncResult(task_id)
    # state = result.state
    # print(state)
    
    return "File Saved"

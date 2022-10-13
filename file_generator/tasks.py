from django.shortcuts import render, HttpResponse
from celery import shared_task
import csv
import random
import string
from django.conf import settings
@shared_task(bind=True)
def generate_file(self, filename, raw_count):

    file_name = str(filename)+".csv"
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = "' + file_name + '"'
    writer = csv.writer(response)
    first_raw = ['Random Data']
    writer.writerow(first_raw)
    for i in range(1, raw_count+1):
        random_raw = [(''.join(random.choices(string.ascii_lowercase, k=5)))]
        writer.writerow(random_raw)

    files_name = file_name.format(settings.MEDIA_ROOT)
    # file = open(files_name, 'w')
    return response

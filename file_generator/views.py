from django.shortcuts import render, HttpResponse
from .tasks import generate_file
import random
import string
import csv


def home(request):
    if request.method == 'POST':
        filename = request.POST.get('file_name')
        raw_count = int(request.POST.get('raw_count'))
        generate_file.delay(filename, raw_count)

        return HttpResponse('Your file Will be download soon')

    return render(request, 'file_generator/csv_generator.html')
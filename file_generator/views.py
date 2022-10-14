from re import template
from django.shortcuts import render, HttpResponse, redirect
from .tasks import generate_file
from .models import *
from celery.result import AsyncResult
from django_celery_results.models import TaskResult

def home(request):
    if request.method == 'POST':
        filename = request.POST.get('file_name')
        raw_count = int(request.POST.get('raw_count'))
        generate_file.delay(filename, raw_count)
       
        return redirect('task_list')

    return render(request, 'file_generator/csv_generator.html')


def task_list(request):
    template_name = 'file_generator/task_result.html'
    task_list = TblCeleryLog.objects.all()
    context = {'task_list':task_list}
    return render(request, template_name, context)

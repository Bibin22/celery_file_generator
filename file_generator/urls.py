from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('task_list', task_list, name='task_list'),
]
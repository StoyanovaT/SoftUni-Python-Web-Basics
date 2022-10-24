from django.shortcuts import render
from django import http

from Django_Project.tasks.models import Task


# Namirame se tuk Django_Project.tasks.views.py


def show_bare_minimum_view(request):
    return http.HttpResponse('It works')


def show_all_tasks(request):
    all_tasks = Task.objects.order_by('id').all()
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)

    return http.HttpResponse(result)


def index(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)


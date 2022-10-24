from django.urls import path

from Django_Project.tasks.views import show_bare_minimum_view, show_all_tasks, index

urlpatterns = (
    path('', index),
    # http://localhost:8000/tasks/it-works/
    path('it-works/', show_bare_minimum_view),
    # http://localhost:8000/tasks/all/
    path('all/', show_all_tasks),
)
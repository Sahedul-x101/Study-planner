from django.urls import path
from tasks.views import create_tasks, view_tasks

urlpatterns = [
    path("create_tasks/", create_tasks),
    path("view_tasks/", view_tasks)
]

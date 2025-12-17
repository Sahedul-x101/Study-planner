from django.urls import path
from tasks.views import create_tasks, tasks_list, mark_complete

urlpatterns = [
    path("create_tasks/", create_tasks, name="create_task"),
    path("tasks_list/", tasks_list, name="task_list"),
    path("complete/<int:task_id>/", mark_complete, name="mark_complete" )
]

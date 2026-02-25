from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def create_tasks(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        completed = request.POST.get('completed') == 'on'
        due_date_str = request.POST.get('due_date')
        priority = request.POST.get('priority', 'medium')
        duration = request.POST.get("duration")

        if duration:
            duration = int(duration)
        else:
            duration = None

        if due_date_str:
            due_date = timezone.make_aware(
                timezone.datetime.strptime(due_date_str, "%Y-%m-%d")
            )
        else:
            due_date = None

        completed_at = timezone.now() if completed else None

        if title:
            Task.objects.create(
                title = title,
                description = description,
                completed = completed,
                completed_at = completed_at,
                due_date = due_date,
                priority = priority,
                duration = duration
            )

            return redirect("task_list")

            
    return render(request, "tasks/create_task.html")

@login_required
def tasks_list(request):
    tasks = Task.objects.filter(completed=False).order_by('-created_at')

    return render(request, "tasks/task_list.html", {"tasks":tasks, "show_header": True})

def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.completed_at = timezone.now()
    task.save()

    return redirect(request.META.get('HTTP_REFERER', 'task_list'))


    

        
from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task


# Create your views here.
def create_tasks(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        completed = request.POST.get('completed') == 'on'

        if title:
            task = Task.objects.create(
                title = title,
                description = description,
                completed = completed
            )
            
    return render(request, 'tasks/task.html')

def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/taskView.html', {'tasks':tasks})
    
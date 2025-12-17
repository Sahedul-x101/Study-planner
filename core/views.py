from django.shortcuts import render
from tasks.models import Task
from datetime import datetime, timedelta
# Create your views here.

def home(request):
    today = datetime.today()
    days_since_sunday = (today.weekday() + 1) % 7
    start_week = today - timedelta(days=days_since_sunday)
    week_days = []

    for i in range(7):
        day = start_week + timedelta(days=i)
        tasks = Task.objects.filter(due_date=day.date(), completed = False)
        week_days.append({"date":day, "day_name": day.strftime("%a"),"tasks":tasks})

    # Task stats
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    pending_tasks = Task.objects.filter(completed=False).count()
    
    top_tasks = Task.objects.filter(completed=False).order_by('-created_at')[:3]

    return render(request, "core/dashboard.html", {"total_tasks":total_tasks, "completed_tasks":completed_tasks, "pending_tasks":pending_tasks,
    "top_tasks": top_tasks,
    "week_days": week_days,
    })

def timer(request):
    return render(request, "core/timer.html")
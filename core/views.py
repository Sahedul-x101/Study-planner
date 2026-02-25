from django.shortcuts import render, redirect
from tasks.models import Task
from datetime import datetime, timedelta
from collections import defaultdict
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    today = datetime.today()

    # ---- Week range (Sunday → Saturday) ----
    days_since_sunday = (today.weekday() + 1) % 7
    start_week = today - timedelta(days=days_since_sunday)
    end_week = start_week + timedelta(days=6)

    # Only current user's tasks
    user_tasks = Task.objects.filter(user=request.user)

    # ---- Weekly tasks (only incomplete + user specific) ----
    week_tasks = user_tasks.filter(
        due_date__range=(start_week.date(), end_week.date()),
        completed=False
    ).only('id', 'title', 'priority', 'due_date')

    # ---- Group by date ----
    tasks_by_date = defaultdict(list)
    for task in week_tasks:
        tasks_by_date[task.due_date].append(task)

    week_days = [
        {
            "date": (day := start_week + timedelta(days=i)),
            "day_name": day.strftime("%a"),
            "tasks": tasks_by_date.get(day.date(), [])
        }
        for i in range(7)
    ]

    # ---- Statistics (USER ONLY) ----
    stats = user_tasks.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(completed=True))
    )

    total_tasks = stats['total']
    completed_tasks = stats['completed']
    pending_tasks = total_tasks - completed_tasks

    # ---- Top 3 recent incomplete tasks (USER ONLY) ----
    top_tasks = user_tasks.filter(completed=False)\
        .only('id','title','priority','created_at','description','due_date','duration')\
        .order_by('-created_at')[:3]

    return render(request, "core/dashboard.html", {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "top_tasks": top_tasks,
        "week_days": week_days,
        "show_header": True,
    })

@login_required
def timer(request):
    return render(request, "core/timer.html", {"show_header": True})


def landing_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # sends logged-in users to dashboard
    return render(request, "core/landing.html")
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

# Registration view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login immediately
            messages.success(request, "Account created successfully!")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")




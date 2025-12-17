from django.urls import path
from core.views import home, timer

urlpatterns = [
    path("", home, name="home"),
    path("timer/", timer, name="timer")
]


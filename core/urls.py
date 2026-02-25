from django.urls import path
from core.views import home, timer, landing_view

urlpatterns = [
    path('', landing_view, name='landing'), 
    path("home/", home, name="home"),
    path("timer/", timer, name="timer"),
]


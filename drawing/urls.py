from django.urls import path
from . import views

urlpatterns = [
    path('', views.canvas_view, name='canvas'),
]
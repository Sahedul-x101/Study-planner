from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path("delete/<int:id>/", views.delete_note),
    path("color/<int:id>/<str:color>/", views.change_color),
]
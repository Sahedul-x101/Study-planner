from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note


@login_required
def note_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        color = request.POST.get("color") or "#ffd966"

        Note.objects.create(
            user=request.user,
            title=title,
            content=content,
            color=color
        )

        return redirect("note_list")

    notes = Note.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "notes/note_list.html", {
        "notes": notes,
        "show_header": True
    })


@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    note.delete()
    return redirect("note_list")


@login_required
def change_color(request, id, color):
    note = get_object_or_404(Note, id=id, user=request.user)
    note.color = color
    note.save()
    return redirect("note_list")
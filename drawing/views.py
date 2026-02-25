from django.shortcuts import render

def canvas_view(request):
    return render(request, 'drawing/canvas.html',{"show_header": True})
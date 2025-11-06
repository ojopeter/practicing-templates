from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.order_by('-date_created')
    return render(request, "tasks/home.html",{'tasks':tasks})

def add_task(request):
    if request.method =="POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_home")
    return render(request, "tasks/add.html")

def mark_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed= True
    task.save()
    return redirect("task_home")

def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_home")
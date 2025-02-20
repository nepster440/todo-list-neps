from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all() # Database se saare tasks le raha hai
    print(tasks) # for debugging
    return render(request, 'to_do/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # ✅ Redirect if form is valid
    else:
        form = TaskForm()  # ✅ Ye sirf GET request me chalega

    return render(request, 'to_do/add_task.html', {'form': form})  # ✅ Yeh har condition me return karega

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete() # Task delete kar raha hai
    return redirect('task_list')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Error Handle karne ke liye
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Existing task ko form me dalo
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Update hone ke baad waps list pe jao
    else:
        form = TaskForm(instance=task)  # Task ke existing data ke saath formbanao
    return render(request, 'to_do/update_task.html', {'form': form, 'task': task})
# Create your views here.

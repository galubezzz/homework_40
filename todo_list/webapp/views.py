from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task


# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    return render(request, 'task.html', context={
        'task': task
    })


def update_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == "GET":
        return render(request, 'update.html', context={
            'task': task
        })
    elif request.method == "POST":
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_view', task_pk=task.pk)


def create_view(request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Task.objects.create(name=name, description=description, status=status)

        return redirect('index')


def delete_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'delete_task.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
    return redirect('index')


def delete_done(request):
    if request.method == 'GET':
        done_tasks = Task.objects.filter(status='done')
        context = {
            'done_tasks': done_tasks
        }

        return render(request, 'delete_done.html', context)

    elif request.method == 'POST':
        if request.POST.get('delete') == "yes":
            done_tasks = Task.objects.filter(status='done')
            done_tasks.delete()
        return redirect('index')
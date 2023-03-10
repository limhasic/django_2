from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
#from django.http import HttpResponse
#from django.shortcuts import render
#from .forms import UploadFileForm
#from .forms import DocumentForm

# Create your views here.

# 1 전체 조회
def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html', {'todos':todos})

# 2 상세 조회
def todo_detail(request, pk):
    todo = Todo.objects.get(id = pk)
    return render(request, 'todo/todo_detail.html' , {'todo':todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST )
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})


def todo_edit(request, pk):
    todo = Todo.objects.get(id= pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})


def todo_done(request, pk):
    todo = Todo.objects.get(id = pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')

def todo_done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/todo_done_list.html', {'dones': dones})

def upload_file(request):
    pass

from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/list.html', {'todos':todos})

def detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/detail.html', {'todo':todo})

def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('list')
    else:
        form = TodoForm()
    return render(request, 'todo/create.html', {'form':form})
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/list.html', {'todos':todos})

def detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/detail.html', {'todo':todo})

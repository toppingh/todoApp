from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/list.html', {'todos':todos})
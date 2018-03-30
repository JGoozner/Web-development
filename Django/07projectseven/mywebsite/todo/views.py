from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
#from django.http import HttpResponse
# Create your views here.
from .forms import TodoForm
from .models import Todo

def index(request):
    mytodo = Todo.objects.order_by('id')
    form= TodoForm()
    context ={ 'mytodo' : mytodo, 'form' : form}
    return render(request, 'todo/index.html', context)

@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)

    #checks if valid
    #***look up santization of input**
    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id) # gets prim id
    mytodo.complete = True # part of models.py
    mytodo.save() #need to save ( does not do that unless stated)
    return redirect('index')

def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def resetTodo(request):
    Todo.objects.filter().delete()
    return redirect('index')

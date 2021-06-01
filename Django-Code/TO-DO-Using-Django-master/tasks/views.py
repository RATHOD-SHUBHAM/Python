from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all() # from template pass into views

    # step 16 :

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        # save the form
        if form.is_valid():
            form.save()
        # if the request method is post we want to return to same view but as get method
        return redirect('/')

    context = {'tasks':tasks, 'form' : form} # from temp pass into views

    # step 10 :
    return render(request,'tasks/list.html',context)

# this part is to edit
def updateTask(request,pk):
    # step 17
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'tasks/update_tasks.html',context)


def deleteTask(request,pk):
    # step 18 :
    item = Task.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request,'tasks/delete.html',context)
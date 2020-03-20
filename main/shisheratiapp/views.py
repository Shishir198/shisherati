from django.shortcuts import render, HttpResponse, redirect
from .models import Task
from .forms import Taskform

# Create your views here.
def first(request):

    if request.method=="POST":
        f = Taskform(request.POST or None)
        if f.is_valid():
            f.save(commit=False).owner = request.user
            f.save()
        return redirect("/app")

    else:
        taskobj = Task.objects.filter(owner = request.user)
        return render(request,'app.html',{'task':taskobj})

def delete(request,idno):
    obj = Task.objects.get(pk = idno)
    obj.delete()

    return redirect("/app")
def edit(request,idno):
    if request.method=="POST":
        new  = Task.objects.get(pk=idno)
        f = Taskform(request.POST or None,instance=new)
        if f.is_valid():
            f.save()

        return redirect("/app")

    else:
        tobj = Task.objects.get(pk=idno)
        return render(request,'edit.html',{'task':tobj})




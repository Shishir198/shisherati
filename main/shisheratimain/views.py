from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages


def home(request):
    return render(request,'homeindex.html')

def register(request):
    if request.method == "POST":

        username =  request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:

                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
            # else:
            #     messages.success(request,"Username already taken")
        else:
            messages.success(request,"Password doesn't matched")

        return redirect("/registration")


    else:
        # return HttpResponse("abcd")
       return render(request,'register.html')


def login(request):

    if request.method =='POST':

        email = request.POST['email']
        password = request.POST['password']

        user  = auth.authenticate(request,username=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("app/")
        else:
            return HttpResponse("invalid ")


    else:
        return render(request,'login.html')


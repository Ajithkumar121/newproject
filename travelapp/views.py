from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from progress.colors import green
from termcolor import colored

from .models import place, Team
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    obj=place.objects.all()
    chara=Team.objects.all()
    return render(request,"index.html",{"result":obj,"team":chara})

def news(request):
    return render(request,"news.html")
def elements(request):
    return render(request,"elements.html")
def contact(request):
    return render(request,"contact.html")

def destination(request):
    return render(request,"destinations.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username")
            return redirect('login')
    return render(request,"login.html")

def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name= request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect("registration")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect("registration")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not matched")
            return redirect('registration')

    return render(request,"registration.html")



def logout(request):
    auth.logout(request)
    return redirect('/')



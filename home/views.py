from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.

def home(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.create_user(username,email,password)
                user.save()
                return HttpResponse("User created sucessfully")
            except IntegrityError:
                return HttpResponse("User already exists")
    
    else:
        form = RegisterForm()

    return render(request, "home.html", {"form":form})

def login(request):
    return HttpResponse("login")

def register(request):
    return render(request, "register.html")
from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("home")

def login(request):
    return HttpResponse("login")

def register(request):
    return render(request, "register.html")
from django.shortcuts import render, HttpResponse
from .models import exercise
# Create your views here.
def home(request):
    exercises = exercise.objects.all()
    return render(request, "home.html", {"exercises": exercises})
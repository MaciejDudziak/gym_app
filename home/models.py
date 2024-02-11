from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default="")

class User_sessions(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default="")

class Session_exercise(models.Model):
    session_id = models.ForeignKey(User_sessions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rep_number = models.IntegerField()
    series_number = models.IntegerField()
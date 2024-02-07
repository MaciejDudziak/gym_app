from django.db import models

# Create your models here.
class exercise(models.Model):
    name = models.CharField(max_length=100)
    rep_number = models.IntegerField()
    series_number = models.IntegerField()
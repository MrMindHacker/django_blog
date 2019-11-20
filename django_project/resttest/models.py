from django.db import models

# Create your models here.


class Car(models.Model):
    """docstring for Car."""
    name = models.CharField(max_length=100)
    top_speed = models.IntegerField()

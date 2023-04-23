from django.db import models

class Flows(models.Model):
    code = models.CharField(max_length=2)
    year = models.IntegerField()
    name = models.CharField(max_length=100)
    flw = models.BinaryField()

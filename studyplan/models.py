from django.db import models

class Flows(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=100)
    flw = models.BinaryField()
    
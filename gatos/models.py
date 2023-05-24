from django.db import models

# Create your models here.

class Gato(models.Model):
    name = models.CharField(max_length=15)
    image = models.URLField()
    ataque = models.SmallIntegerField()
    defensa = models.SmallIntegerField()
    tipo = models.CharField(max_length=15)
    counter = models.CharField(max_length=15)
    strong = models.CharField(max_length=15)
    
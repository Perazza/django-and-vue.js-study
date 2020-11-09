from django.db import models

# Create your models here.

class Games(models.Model):
    titulo = models.CharField(max_length=200)
    plataformas = models.CharField(max_length=200)

    def __str__(self):
        return self.name


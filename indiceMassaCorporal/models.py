from django.db import models

class CalcularIMC(models.Model):
    peso = models.FloatField('peso')
    altura = models.FloatField('altura')
from django.db import models
from decimal import Decimal
# Create your models here.

class graph(models.Model):
    title = models.CharField(max_length=50, null=True)
    x_axis_title = models.CharField(max_length=50)
    y_axis_title = models.CharField(max_length=50)

class x_axis_labels(models.Model):
    graph = models.ForeignKey(graph, on_delete=models.CASCADE, verbose_name= 'IdGraph') #Muchos a uno
    label = models.CharField(max_length=50)

class y_axis_labels(models.Model):
    graph = models.ForeignKey(graph, on_delete=models.CASCADE, verbose_name= 'IdGraph') #Muchos a uno
    label = models.CharField(max_length=50)

class year(models.Model):
    graph = models.ForeignKey(graph, on_delete=models.CASCADE, verbose_name= 'IdGraph') #Muchos a uno
    year = models.IntegerField(null=True, blank=True)

class entity(models.Model):
    graph = models.ForeignKey(graph, on_delete=models.CASCADE, verbose_name= 'IdGraph') #Muchos a uno
    year = models.ManyToManyField(year) #Muchos a muchos
    Entity = models.CharField(max_length=50)

class census(models.Model):
    graph = models.ForeignKey(graph, on_delete=models.CASCADE, verbose_name= 'IdGraph') #Muchos a uno
    years = models.ForeignKey(year,on_delete=models.CASCADE, verbose_name= 'IdYear') #Muchos a uno
    entity = models.ForeignKey(entity,on_delete=models.CASCADE, verbose_name= 'IdEntity') #Muchos a uno
    data = models.DecimalField(max_digits=2, decimal_places=1)




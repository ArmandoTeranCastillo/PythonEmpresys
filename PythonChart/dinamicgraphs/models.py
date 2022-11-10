from django.db import models
from django.contrib.postgres.fields import ArrayField

#Definir los modelos. Con ellos podremos organizar,
#almacenar y migrar nuestra informacion desde una base de datos
#hasta las views que podra ver el usuario
class graph(models.Model):
    title = models.CharField(max_length=50)
    x_axis_title = models.CharField(max_length=50)
    y_axis_title = models.CharField(max_length=50)

    x_axis_range_start =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    x_axis_range_end = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    y_axis_range_start =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    y_axis_range_end = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    
    year_range_start = models.IntegerField(null=True, blank=True)
    year_range_end = models.IntegerField(null=True, blank=True)
    

#Censo de poblacion por genero en cada estado de Mexico
class censuspoblation(models.Model):
    title = models.CharField(max_length=50)
    state_title = models.CharField(max_length=50)
    gender_title = models.CharField(max_length=50)
    census = models.DecimalField(max_digits=10, decimal_places=2, default=0)

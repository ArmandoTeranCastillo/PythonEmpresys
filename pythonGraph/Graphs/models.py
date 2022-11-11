from django.db import models
from django.contrib.postgres.fields import ArrayField
from decimal import Decimal
#Definir los modelos. Con ellos podremos organizar,
#almacenar y migrar nuestra informacion desde una base de datos
#hasta las views que podra ver el usuario
class graph(models.Model):
    title = models.CharField(max_length=50) #Nombre de la grafica
    x_axis_title = models.CharField(max_length=50) #Titulo del Eje X
    y_axis_title = models.CharField(max_length=50) #Titulo del Eje Y

    x_axis_values = ArrayField( #Lista de valores del Eje X
            models.CharField(max_length=50),
            size= 1 #Dimension de la lista
    ) 
    y_axis_values = ArrayField( #Lista de valores del Eje Y
            models.CharField(max_length=50),
            size= 1 
    ) 

    year = models.IntegerField(null=True, blank=True) #Año del censo

    censusdata = ArrayField( #Lista de valores del censo
            models.CharField(max_length=50),
            size= 1 #Dimension de la lista
    ) 


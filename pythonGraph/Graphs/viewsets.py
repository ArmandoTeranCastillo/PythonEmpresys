from .models import *
from .serializer import *
from rest_framework import viewsets
#VISTA
#Permite realizar un CRUT sobre nuestros objetos
#Crear, actualizar, consultar y eliminar datos de los objetos
class graphViewSet(viewsets.ModelViewSet):
    queryset = graph.objects.all()
    serializer_class = graphSerializer
class x_axis_label_ViewSet(viewsets.ModelViewSet):
    queryset = x_axis_labels.objects.all()
    serializer_class = x_axis_labelsSerializer
class y_axis_label_ViewSet(viewsets.ModelViewSet):
    queryset = y_axis_labels.objects.all()
    serializer_class = y_axis_labelSerializer
class yearViewSet(viewsets.ModelViewSet):
    queryset = year.objects.all()
    serializer_class = yearSerializer   
class entityViewSet(viewsets.ModelViewSet):
    queryset = entity.objects.all()
    serializer_class = entitySerializer
class censusViewSet(viewsets.ModelViewSet):
    queryset = census.objects.all()
    serializer_class = censusSerializer
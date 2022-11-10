from .models import graph, censuspoblation
from .serializer import graphSerializer, censusSerializer
from rest_framework import viewsets

#Permite realizar un CRUT sobre nuestros objetos
#Crear, actualizar, consultar y eliminar datos de los objetos
class graphViewSet(viewsets.ModelViewSet):
    queryset = graph.objects.all()
    serializer_class = graphSerializer

class censusViewSet(viewsets.ModelViewSet):
    queryset = censuspoblation.objects.all()
    serializer_class =  censusSerializer
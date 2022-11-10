from .models import graph, censuspoblation
from rest_framework import serializers

#Permite preparar nuestros modelos para ser transfortados
#Via HTTPS
class graphSerializer(serializers.ModelSerializer):
    class Meta:
        model = graph
        fields = '__all__'

class censusSerializer(serializers.ModelSerializer):
    class Meta:
        model = censuspoblation
        fields = '__all__'
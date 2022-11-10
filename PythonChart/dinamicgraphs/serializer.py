from .models import graph
from rest_framework import serializers

#Permite preparar nuestros modelos para ser transfortados
#Via HTTPS
class graphSerializer(serializers.ModelSerializer):
    class Meta:
        model = graph
        fields = '__all__'
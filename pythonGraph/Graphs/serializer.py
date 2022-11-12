from .models import *
from rest_framework import serializers
#CONTROLADOR
#Configura a nuestros modelos para que puedan
#Ser transportados via HTTPS
class graphSerializer(serializers.ModelSerializer):
    class Meta:
        model = graph
        fields = '__all__'

class x_axis_labelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = x_axis_labels
        fields = '__all__'

class y_axis_labelSerializer(serializers.ModelSerializer):
    class Meta:
        model = y_axis_labels
        fields = '__all__'

class yearSerializer(serializers.ModelSerializer):
    class Meta:
        model = year
        fields = '__all__'

class entitySerializer(serializers.ModelSerializer):
    class Meta:
        model = entity
        fields = '__all__'

class censusSerializer(serializers.ModelSerializer):
    class Meta:
        model = census
        fields = '__all__'
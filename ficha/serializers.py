from rest_framework import serializers
from .models import FichaMedica

class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaMedica
        fields = '__all__'
        

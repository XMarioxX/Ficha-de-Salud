from rest_framework import generics
from .models import FichaMedica
from .serializers import FichaMedicaSerializer
from .utils import modify_existing_pdf
import os
from django.conf import settings

class FichaMedicaCreate(generics.CreateAPIView):
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        input_pdf = os.path.join(settings.BASE_DIR, 'formatos', 'Ficha-Salud-2024-1.pdf')
        output_pdf = os.path.join(settings.BASE_DIR, 'output', 'Ficha_de_Salud_Modificada.pdf')
        data = {
            'nombre': instance.nombre,
            'provincia': instance.provincia,
            'cum': instance.cum,
            'fecha_nacimiento': instance.fecha_nacimiento.strftime('%d/%m/%Y'),
            'grupo': instance.grupo,
            'seccion': instance.seccion,
            'alerta': instance.alerta,
        }
        modify_existing_pdf(input_pdf, output_pdf, data)

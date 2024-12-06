from rest_framework import generics
from .models import FichaMedica
from .serializers import FichaMedicaSerializer
from .utils import modify_existing_pdf
import os
from django.conf import settings
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


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
            'grupoRH': instance.grupoRH,
            'peso': instance.peso,
            'talla': instance.talla,
            'imc': instance.imc,
            'alimentacion': instance.alimentacion,
            'nombreProveedorInstituciones': instance.nombreProveedorInstituciones,
            'numeroPolizaProveedorInstituciones': instance.numeroPolizaProveedorInstituciones,
            'derechoHabienciaProveedorInstituciones': instance.derechoHabienciaProveedorInstituciones,
            'observacionesProveedorInstituciones': instance.observacionesProveedorInstituciones,
            
            'nombreProveedorAseguradoras': instance.nombreProveedorAseguradoras,
            'numeroPolizaProveedorAseguradoras': instance.numeroPolizaProveedorAseguradoras,
            'derechoHabienciaProveedorAseguradoras': instance.derechoHabienciaProveedorAseguradoras,
            'observacionesProveedorAseguradoras': instance.observacionesProveedorAseguradoras,
            
            'nombreProveedorParticular': instance.nombreProveedorParticular,
            'numeroPolizaProveedorParticular': instance.numeroPolizaProveedorParticular,
            'derechoHabienciaProveedorParticular': instance.derechoHabienciaProveedorParticular,
            'observacionesProveedorParticular': instance.observacionesProveedorParticular,

            'tratamientosActuales': instance.tratamientosActuales,
            'alergias': instance.alergias,

            'diabetes': instance.diabetes,
            'diabetesEspecifique': instance.diabetesEspecifique,
            'hipertension': instance.hipertension,
            'hipertensionEspecifique': instance.hipertensionEspecifique,
            'eventoEpileptico': instance.eventoEpileptico,
            'eventoEpilepticoEspecifique': instance.eventoEpilepticoEspecifique,
            'problemaCardiaco': instance.problemaCardiaco,
            'problemaCardiacoEspecifique': instance.problemaCardiacoEspecifique,
            'desmayoMareo': instance.desmayoMareo,
            'desmayoMareoEspecifique': instance.desmayoMareoEspecifique,
            'asma': instance.asma,
            'asmaEspecifique': instance.asmaEspecifique,
            'toxicomanias': instance.toxicomanias,
            'toxicomaniasEspecifique': instance.toxicomaniasEspecifique,
            'cirugiaReciente': instance.cirugiaReciente,
            'cirugiaRecienteEspecifique': instance.cirugiaRecienteEspecifique,
            'embarazoPuerperio': instance.embarazoPuerperio,
            'embarazoPuerperioEspecifique': instance.embarazoPuerperioEspecifique,
            'transfucion': instance.transfucion,
            'transfucionEspecifique': instance.transfucionEspecifique,
            'lesionMusculoEsqueletica': instance.lesionMusculoEsqueletica,
            'lesionMusculoEsqueleticaEspecifique': instance.lesionMusculoEsqueleticaEspecifique,
            'ortopedicos': instance.ortopedicos,
            'ortopedicosEspecifique': instance.ortopedicosEspecifique,
            'respiratorios': instance.respiratorios,
            'respiratoriosEspecifique': instance.respiratoriosEspecifique,
            'oftalmicos': instance.oftalmicos,
            'oftalmicosEspecifique': instance.oftalmicosEspecifique,
            'narizOidos': instance.narizOidos,
            'narizOidosEspecifique': instance.narizOidosEspecifique,
            'neurologicos': instance.neurologicos,
            'neurologicosEspecifique': instance.neurologicosEspecifique,
            'hematologicos': instance.hematologicos,
            'hematologicosEspecifique': instance.hematologicosEspecifique,
            'hepaticos': instance.hepaticos,
            'hepaticosEspecifique': instance.hepaticosEspecifique,
            'aparatoDigestivo': instance.aparatoDigestivo,
            'aparatoDigestivoEspecifique': instance.aparatoDigestivoEspecifique,
            'tiroideo': instance.tiroideo,
            'tiroideoEspecifique': instance.tiroideoEspecifique,
            'dermatologico': instance.dermatologico,
            'dermatologicoEspecifique': instance.dermatologicoEspecifique,
            'inmunologicos': instance.inmunologicos,
            'inmunologicosEspecifique': instance.inmunologicosEspecifique,
            'urinarios': instance.urinarios,
            'urinariosEspecifique': instance.urinariosEspecifique,
            'covid': instance.covid,
            'covidEspecifique': instance.covidEspecifique,

            'cambioAlimentacion': instance.cambioAlimentacion,
            'cambioAlimentacionEspecifique': instance.cambioAlimentacionEspecifique,
            'aislamientoPersonal': instance.aislamientoPersonal,
            'aislamientoPersonalEspecifique': instance.aislamientoPersonalEspecifique,
            'sensacionVacio': instance.sensacionVacio,
            'sensacionVacioEspecifique': instance.sensacionVacioEspecifique,
            'impotenciaDesesperanza': instance.impotenciaDesesperanza,
            'impotenciaDesesperanzaEspecifique': instance.impotenciaDesesperanzaEspecifique,
            'confunsion': instance.confunsion,
            'confunsionEspecifique': instance.confunsionEspecifique,
            'pensamiento': instance.pensamiento,
            'pensamientoEspecifique': instance.pensamientoEspecifique,
            'pensarLastimarse': instance.pensarLastimarse,
            'pensarLastimarseEspecifique': instance.pensarLastimarseEspecifique,
            'alteracionesSueño': instance.alteracionesSueño,
            'alteracionesSueñoEspecifique': instance.alteracionesSueñoEspecifique,
            'agotamientoExcesivo': instance.agotamientoExcesivo,
            'agotamientoExcesivoEspecifique': instance.agotamientoExcesivoEspecifique,
            'doloresInexplicables': instance.doloresInexplicables,
            'doloresInexplicablesEspecifique': instance.doloresInexplicablesEspecifique,
            'aumentoToxicomania': instance.aumentoToxicomania,
            'aumentoToxicomaniaEspecifique': instance.aumentoToxicomaniaEspecifique,
            'cambioHumor': instance.cambioHumor,
            'cambioHumorEspecifique': instance.cambioHumorEspecifique,
            'escucharVoces': instance.escucharVoces,
            'escucharVocesEspecifique': instance.escucharVocesEspecifique,
            'dificultadTareasDiarias': instance.dificultadTareasDiarias,
            'dificultadTareasDiariasEspecifique': instance.dificultadTareasDiariasEspecifique,

            'descripcionTratamientoMedico': instance.descripcionTratamientoMedico,

        }

        try:
            modify_existing_pdf(input_pdf, output_pdf, data)
            self.send_email(instance, output_pdf)

        except Exception as e:
            print(f"Error al modificar el PDF o enviar el correo: {e}")

    def send_email(self, instance, output_pdf):
        subject = f'Ficha de Salud de {instance.nombre}'
        message = f'La ficha de salud de {instance.nombre} ha sido creada y se adjunta el PDF modificado.'
        email = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
        )
        email.attach_file(output_pdf) 
        email.send()

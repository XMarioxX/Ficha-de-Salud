from django.db import models

class FichaMedica(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    cum = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    grupo = models.CharField(max_length=10)
    seccion = models.CharField(max_length=50)
    alerta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

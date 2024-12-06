from django.urls import path
from .views import FichaMedicaCreate

urlpatterns = [
    path('api/ficha-medica/', FichaMedicaCreate.as_view(), name='ficha-medica-create'),
]

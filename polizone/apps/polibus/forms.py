from django import forms
from .models import Ruta

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['ruta', 'paradas', 'horario']  # Asegúrate de incluir los campos necesarios

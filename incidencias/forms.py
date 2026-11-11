from django import forms
from .models import Incidencia

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['titulo', 'descripcion', 'prioridad', 'tecnico']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'tecnico': forms.Select(attrs={'class': 'form-control'}),
        }
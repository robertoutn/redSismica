from django import forms
from .models import OrdenInspeccionES

class CierreOrdenInspeccionForm(forms.ModelForm):
    class Meta:
        model = OrdenInspeccionES
        fields = ['comentario_cierre']
        widgets = {
            'comentario_cierre': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ingrese un comentario de cierre...'}),
        }

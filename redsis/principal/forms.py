from django import forms
from .models import OrdenInspeccionES

class CierreOrdenInspeccionForm(forms.ModelForm):
    class Meta:
        model = OrdenInspeccionES
        fields = ['comentario_cierre']
        widgets = {
            'comentario_cierre': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ingrese un comentario de cierre...'}),
        }

    def clean_comentario_cierre(self):
        comentario = self.cleaned_data.get('comentario_cierre')
        if not comentario or not comentario.strip():
            raise forms.ValidationError('El comentario de cierre es obligatorio.')
        return comentario

from django.db import models
from django.contrib.auth.models import Permission

class PermisoExtra(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    permiso = models.OneToOneField(Permission, on_delete=models.CASCADE, related_name='permiso_extra')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Permiso Extra'
        verbose_name_plural = 'Permisos Extras'

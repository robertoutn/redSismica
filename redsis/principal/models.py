from django.db import models
from django.contrib.auth.models import Group, User

# Definición de roles personalizados como grupos
ROLES = [
    'Analista de Sismos',
    'Supervisor',
    'Técnico de Mantenimiento',
    'Administrador',
    'Responsable de Inspección',
    'Interesado',
    'Centro de Control de Red Sísmica (CCRS)'
]

def crear_roles():
    for nombre in ROLES:
        Group.objects.get_or_create(name=nombre)

class OrdenInspeccionES(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    estacion = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    responsable = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ordenes_responsable')
    estado = models.CharField(max_length=30, choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada')], default='abierta')
    comentario_cierre = models.TextField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Orden #{self.numero} - {self.estacion}"

    class Meta:
        verbose_name = 'Orden de Inspección de ES'
        verbose_name_plural = 'Órdenes de Inspección de ES'

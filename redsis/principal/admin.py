from django.contrib import admin
from .models import OrdenInspeccionES

@admin.register(OrdenInspeccionES)
class OrdenInspeccionESAdmin(admin.ModelAdmin):
    list_display = ('numero', 'estacion', 'responsable', 'estado', 'fecha_creacion', 'fecha_cierre')
    list_filter = ('estado', 'estacion')
    search_fields = ('numero', 'estacion', 'responsable__username')
    readonly_fields = ('fecha_creacion', 'fecha_cierre', 'estado', 'comentario_cierre')

from django.contrib import admin
from .models import PermisoExtra

@admin.register(PermisoExtra)
class PermisoExtraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'permiso')
    search_fields = ('nombre',)

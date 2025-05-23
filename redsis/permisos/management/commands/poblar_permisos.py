from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, ContentType
from permisos.models import PermisoExtra
from principal.models import OrdenInspeccionES

class Command(BaseCommand):
    help = 'Crea permisos extra de ejemplo para la app permisos.'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(OrdenInspeccionES)
        ejemplos = [
            ('puede_cerrar_orden', 'Puede cerrar orden de inspección'),
            ('puede_ver_reportes', 'Puede ver reportes de inspección'),
            ('puede_exportar_datos', 'Puede exportar datos de inspección'),
        ]
        for codename, nombre in ejemplos:
            permiso, _ = Permission.objects.get_or_create(
                codename=codename,
                name=nombre,
                content_type=content_type
            )
            PermisoExtra.objects.get_or_create(
                nombre=nombre,
                permiso=permiso,
                descripcion=f'Permiso extra: {nombre}'
            )
        self.stdout.write(self.style.SUCCESS('Permisos extra de ejemplo creados.'))

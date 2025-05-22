from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from principal.models import OrdenInspeccionES

class Command(BaseCommand):
    help = 'Crea datos de ejemplo para órdenes de inspección de ES.'

    def handle(self, *args, **kwargs):
        responsable, _ = User.objects.get_or_create(username='responsable', defaults={
            'email': 'responsable@example.com',
            'is_staff': True,
            'is_superuser': False
        })
        OrdenInspeccionES.objects.get_or_create(
            numero='ES-001', estacion='Estación Norte', responsable=responsable
        )
        OrdenInspeccionES.objects.get_or_create(
            numero='ES-002', estacion='Estación Sur', responsable=responsable
        )
        self.stdout.write(self.style.SUCCESS('Órdenes de inspección de ejemplo creadas.'))

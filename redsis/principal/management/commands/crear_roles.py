from django.core.management.base import BaseCommand
from principal.models import crear_roles

class Command(BaseCommand):
    help = 'Crea los grupos de roles principales para el sistema.'

    def handle(self, *args, **kwargs):
        crear_roles()
        self.stdout.write(self.style.SUCCESS('Roles principales creados o actualizados.'))

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import OrdenInspeccionES
from .forms import CierreOrdenInspeccionForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def es_responsable(user):
    return user.groups.filter(name__in=["Responsable de Inspección", "Administrador"]).exists() or user.is_superuser

def es_responsable_de_orden(user, orden):
    return user == orden.responsable or user.is_superuser

@login_required
@user_passes_test(es_responsable)
def cerrar_orden_inspeccion(request, pk):
    orden = get_object_or_404(OrdenInspeccionES, pk=pk)
    if not es_responsable_de_orden(request.user, orden):
        messages.error(request, 'Solo el responsable asignado puede cerrar esta orden.')
        return redirect('ordenes_listar')
    if orden.estado == 'cerrada':
        messages.error(request, 'La orden ya está cerrada.')
        return redirect('ordenes_listar')
    if request.method == 'POST':
        form = CierreOrdenInspeccionForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.estado = 'cerrada'
            orden.fecha_cierre = timezone.now()
            orden.save()
            messages.success(request, 'La orden fue cerrada exitosamente.')
            return redirect('ordenes_listar')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = CierreOrdenInspeccionForm(instance=orden)
    return render(request, 'principal/cerrar_orden.html', {'form': form, 'orden': orden})

@login_required
def ordenes_listar(request):
    ordenes = OrdenInspeccionES.objects.all().order_by('-fecha_creacion')
    return render(request, 'principal/ordenes_listar.html', {'ordenes': ordenes})

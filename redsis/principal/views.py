from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import OrdenInspeccionES
from .forms import CierreOrdenInspeccionForm

@login_required
def cerrar_orden_inspeccion(request, pk):
    orden = get_object_or_404(OrdenInspeccionES, pk=pk)
    if request.method == 'POST':
        form = CierreOrdenInspeccionForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.estado = 'cerrada'
            orden.fecha_cierre = timezone.now()
            orden.save()
            return redirect('ordenes_listar')
    else:
        form = CierreOrdenInspeccionForm(instance=orden)
    return render(request, 'principal/cerrar_orden.html', {'form': form, 'orden': orden})

@login_required
def ordenes_listar(request):
    ordenes = OrdenInspeccionES.objects.all().order_by('-fecha_creacion')
    return render(request, 'principal/ordenes_listar.html', {'ordenes': ordenes})

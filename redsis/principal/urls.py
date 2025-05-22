from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('ordenes_listar'), name='home'),
    path('ordenes/', views.ordenes_listar, name='ordenes_listar'),
    path('ordenes/<int:pk>/cerrar/', views.cerrar_orden_inspeccion, name='cerrar_orden_inspeccion'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

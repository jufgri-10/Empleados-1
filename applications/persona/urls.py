from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'empleados-todos/',
        views.ListAllEmpleados.as_view(),
        name='empleados_todos'
    ),
    path(
        'empleados-area/<name>/',
        views.ListByArea.as_view(),
        name='area'
    ),
    path(
        'empleados-buscar/',
        views.ListByKword.as_view(),
        name='buscar'
    ),
    path(
        'empleados-habilidad/',
        views.ListByHabilidad.as_view(),
        name='habilidad'
    ),
    path('ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='detail'
    ),
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='agregar'
    ),
    path(
        'modificar-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'success',
        views.SuccessView.as_view(),
        name='correcto'
    ),
    path(
        'eliminar/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
    path(
        'empleados-administrar/',
        views.ListEmpleadosAd.as_view(),
        name='empleados_administrar'
    ),
]
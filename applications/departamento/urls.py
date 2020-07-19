from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

def DesdeApps(self):
    print('============= desde la app departamento ============')

urlpatterns = [
    path(
        'departamento/',
        DesdeApps,
        name='departamento'
    ),
    path(
        'new-departamento/',
        views.NewDepartamentoView.as_view(),
        name='new_departamento'
    ),
    path(
        'lista-d/',
        views.DepartamentoListView.as_view(),
        name='lista_d'
    )
]
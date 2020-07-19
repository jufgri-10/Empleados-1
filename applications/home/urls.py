from django.contrib import admin
from django.urls import path
from . import views

app_name = 'prueba_app'

urlpatterns = [
    path(
        'prueba/',
        views.PruebaView.as_view(),
        name='prueba_home'
    ),
    path(
        'lista/',
        views.PruebaListView.as_view()),
    path(
        'lista-prueba/',
        views.ListarPrueba.as_view()),
    path(
        'add/',
        views.PruebaCreateView.as_view(),
        name='prueba_add'
    ),
    path(
        'foundation/',
        views.ResumeFoundationView.as_view(),
        name='rf'
        ),
]
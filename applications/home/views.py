from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
# Importar Modelos
from .models import Prueba
from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

class PruebaListView(ListView):
    #model = MODEL_NAME se usa para bases de datos
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30', '40', '50']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url = reverse_lazy('prueba_app:prueba_home')
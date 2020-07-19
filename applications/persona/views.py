from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado

# Create your views here.

class InicioView(TemplateView):
    """ Vista pagina inicio """
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 7
    ordering = 'last_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

class ListEmpleadosAd(ListView):
    template_name = 'persona/list_ad.html'
    paginate_by = 7
    ordering = 'last_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

class ListByArea(ListView):
    template_name = 'persona/list_area.html'
    context_object_name = 'empleados'
        
    def get_queryset(self):
        dep_clave = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name=dep_clave
        )
        return lista

class ListByKword(ListView):
    template_name = 'persona/list_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword',)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

class ListByHabilidad(ListView):
    template_name = 'persona/list_habilidad.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        em_clave = self.request.GET.get('clave')
        empleado = Empleado.objects.get(id = em_clave)
        return empleado.habilidades

class EmpleadoDetailView(DetailView):
    template_name = 'persona/detail_empleado.html' 
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = '- Empleado del Mes'
        return context

class SuccessView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = ('__all__')
    """ Para elegir campos especificos
    fields = [
        'first_name'
        'last_name'
        'phone'
        'adress'
    ] """
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.save
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

class EmpleadoDeleteView(DeleteView):
    template_name = 'persona/eliminar.html'
    model = Empleado
    success_url = reverse_lazy('persona_app:correcto')
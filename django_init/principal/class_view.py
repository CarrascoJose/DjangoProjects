from django.shortcuts import redirect, render
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import Persona
from .forms import PersonaForm


"""
Clase padre de las cuales las clases de vistas heredan
class View():
    dispatch: verificar el metodo de la solicitud http
    http_not_allowed        
"""

class PersonaList(ListView):
    model = Persona
    template_name = 'principal/index.html'

    def get_queryset(self):
        return self.model.objects.all()


class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'principal/crear_persona.html'
    success_url = reverse_lazy('index2')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'principal/crear_persona.html'
    success_url = reverse_lazy('index2')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index2')
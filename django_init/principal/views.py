from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Persona
from .forms import PersonaForm
# Create your views here.

def start(request):
    personas = Persona.objects.all() #select * from Persona

    contexto = {
        "personas":personas,
    }
    return render(request,'principal/index.html',contexto)
    
def crearPersona(request):
    if request.method == "GET":
        form = PersonaForm()
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'principal/crear_persona.html',contexto)

def editarPersona(request,id):
    persona = Persona.objects.get(id=id)
    if request.method=="GET":
        form = PersonaForm(instance=persona)
        contexto = {'form':form}
    
    else:
        form = PersonaForm(request.POST, instance=persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'principal/crear_persona.html',contexto)

def eliminarPersona(request,id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('index')

from django.shortcuts import render, redirect
from django.views import generic
from .models import Juego
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'catalogo/index.html')

def PlayStation(request):
    return render(request, 'catalogo/PlayStation.html')

def Xbox(request):
    return render(request, 'catalogo/Xbox.html')

def Switch(request):
    return render(request, 'catalogo/Switch.html')

def Formulario(request):
    return render(request, 'catalogo/Formulario.html')

def Carro(request):
    return render(request, 'catalogo/Carro.html')

#crud de juegos

def AgregarJuego(request):
    return render(request, 'catalogo/Agregar.html')

def ListaJuegos(request):

    juego = Juego.objects.all()


    return render(request, 'catalogo/ListaJuegos.html', {
             'juego':juego
                    })
def Eliminar_juego(request, id):    
    #buscar juego para eliminar
    juego1 = Juego.objects.get(id=id)

    try:
        juego1.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)

    except:
        mensaje = "no se a podido eliminar" 
        messages.error(request, mensaje)
    
    return redirect('ListaJuegos')
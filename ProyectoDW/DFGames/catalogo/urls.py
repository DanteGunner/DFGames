from django.urls import path
from . import views
from . views import PlayStation,Xbox,Switch,Formulario,Carro,ListaJuegos,Eliminar_juego,AgregarJuego
urlpatterns=[
    path('', views.index, name='index'),
	path('PlayStation', PlayStation, name='PlayStation'),
    path('Xbox', Xbox, name='Xbox'),
    path('Switch', Switch, name='Switch'),
    path('Formulario', Formulario, name='Formulario'),
    path('Carro', Carro, name='Carro'),	
    path('ListaJuegos', ListaJuegos, name="ListaJuegos"),
    path('Eliminar_juego/<id>/', Eliminar_juego, name="Eliminar_juego"),
    path('Agregar', AgregarJuego, name="AgregarJuego"),
]
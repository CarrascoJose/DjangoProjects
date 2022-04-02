from django.urls import path
from . import views

urlpatterns = [
    path('inicio/',views.start,name="index"),
    path('agregar_persona',views.crearPersona,name="crear"),
    path('editar_persona/<int:id>',views.editarPersona,name="editar"),
    path('eliminar_persona/<int:id>',views.eliminarPersona,name="eliminar")
]
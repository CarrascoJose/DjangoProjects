from django.urls import path
from . import views
from . import class_view

urlpatterns = [
    path('inicio/',views.start,name="index"),
    path('agregar_persona',views.crearPersona,name="crear"),
    path('editar_persona/<int:id>',views.editarPersona,name="editar"),
    path('eliminar_persona/<int:id>',views.eliminarPersona,name="eliminar"),
    #AQUI SE SEPARA LO QUE ES VISTAS EN FUNCIONES, Y ABAJO LAS VISTAS EN CLASES
    path('mostrar_personas',class_view.PersonaList.as_view(),name="index2"),
    path('agregar_persona2',class_view.PersonaCreate.as_view(),name="crear2"),
    path('editar_persona2/<int:pk>',class_view.PersonaUpdate.as_view(),name="editar2"),
    path('editar_persona2/<int:pk>',class_view.PersonaDelete.as_view(),name="eliminar2")

]
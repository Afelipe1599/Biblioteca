from django.urls import path, re_path
from .views import crearAutor,listarAutor,editarAutor,eliminarAutor

urlpatterns = [
    path('crear_autor/',crearAutor, name = 'crear_autor'),
    path('listar_autor/',listarAutor, name = 'listar_autor'),
    path('editar_autor/<int:id>',editarAutor, name = 'editar_autor'),
    path('eliminarAutor/<int:id>',eliminarAutor, name = 'eliminar_autor')
    
]
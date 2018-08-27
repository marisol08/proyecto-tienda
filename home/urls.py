from django.urls import path 
from .views import *
urlpatterns = [
	path('quienes_somos/', quienes_somos_view, name='quienes_somos'),
	path('contactenos/', contacto_view, name='contacto'),
	path('lista_productos/', lista_productos_view, name = 'lista_productos'),
	path('agregar_producto/', agregar_producto_view, name = 'agregar_producto'),
	path('ver_producto/<int:id_prod>/', ver_producto_view, name = 'ver_producto'),
	path('editar_producto/<int:id_prod>/', editar_producto_view, name = 'editar_producto'),
	path('eliminar_producto/<int:id_prod>/', eliminar_producto_view, name = 'eliminar_producto'),

	path('desactivar_producto/<int:id_prod>/', desactivar_producto_view, name = 'desactivar_producto'),
]  
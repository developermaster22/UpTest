from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
     path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_productos'),

   
]

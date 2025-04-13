from django.contrib import admin
from .models import Producto

admin.site.register(Producto)
#registramos nuestro modelo Producto en el admin de django para que se pueda ver y editar desde la interfaz de administración.
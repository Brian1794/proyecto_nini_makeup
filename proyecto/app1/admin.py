from django.contrib import admin
from .models import Usuarios  # Asegúrate de importar tu modelo

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'celular', 'email', 'direccion')

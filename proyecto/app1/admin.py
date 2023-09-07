from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellidos', 'celular', 'email', 'direccion', 'contraseña', 'estado', 'created_at')

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from app1.models import Usuarios

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        contraseña = request.POST.get('contraseña')

        # Hashear la contraseña antes de guardarla en la base de datos
        contraseña_hasheada = make_password(contraseña)

        # Crear un nuevo usuario con los datos proporcionados
        nuevo_usuario = Usuarios(nombre=nombre, apellidos=apellidos, celular=celular, email=email, direccion=direccion, contraseña=contraseña_hasheada)
        nuevo_usuario.save()

        messages.success(request, '¡usuario registrado exitosamente!')
        return render(request, 'registro.html')
    else:
        messages.success(request, '¡ya estas registrado!')
        return render(request, 'registro.html')
        



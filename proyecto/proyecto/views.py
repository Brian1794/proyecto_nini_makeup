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
        contrasena = request.POST.get('contrasena')

        # Hash the password before saving it to the database
        contrasena_hasheada = make_password(contrasena)

        # Create a new user with the data provided
        nuevo_usuario = Usuarios(nombre=nombre, apellidos=apellidos, celular=celular, email=email, direccion=direccion, contrasena=contrasena_hasheada)
        nuevo_usuario.save()

        messages.success(request, '¡Usuario registrado exitosamente!')
        return render(request, 'registro.html')
    else:
        messages.success(request, '¡Ya estás registrado!')
        return render(request, 'registro.html')
    
    
 
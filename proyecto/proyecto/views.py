from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from app1.models import Usuarios
from django.shortcuts import render, redirect, get_object_or_404
from app1.models import Usuarios


# registro de usuarios

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        contrasena = request.POST.get('contrasena')

        # Hashear la contraseña antes de guardarla en la base de datos
        contrasena_hasheada = make_password(contrasena)

        # Crear un nuevo usuario con los datos proporcionados
        nuevo_usuario = Usuarios(nombre=nombre, apellidos=apellidos, celular=celular, email=email, direccion=direccion, contrasena=contrasena_hasheada)
        nuevo_usuario.save()

        messages.success(request, '¡usuario registrado exitosamente!')
        return render(request, 'registro.html')
    else:
        
        messages.success(request, '¡ya estas registrado!')
        return render(request, 'registro.html')
        


# Vista para listar todos los usuarios

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

# Vista para crear un nuevo usuario

def agregar_usuario(request):
    if request.method == 'POST':
        formulario = AddUsuariosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect("listar_usuarios")  # Reemplaza "listar_usuarios" con la URL adecuada
    else:
        formulario = AddUsuariosForm()
    
    return render(request, 'agregar_usuario.html', {'formulario': formulario})

# Vista para editar un usuario

def form_editar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, idestudios=id)
    if request.method == 'POST':
        formulario = AddUsuariosForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario editado exitosamente')
            return redirect("listar_usuarios")  # Reemplaza "listar_usuarios" con la URL adecuada
    else:
        formulario = AddUsuariosForm(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'formulario': formulario, 'usuario': usuario})

# Vista para eliminar un usuario

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, idestudios=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return redirect("listar_usuarios")  # Reemplaza "listar_usuarios" con la URL adecuada
    
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})

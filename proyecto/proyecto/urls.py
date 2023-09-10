

"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    """

from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from proyecto.views import registro
from proyecto.views import inicio
=======
>>>>>>> c348d75c42ef95f039be2ec4ebdc54f9761d9a36
from . import views  # Importa las vistas desde la aplicación app1
from proyecto.views import valida_login


urlpatterns = [
    
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('inicio/', views.inicio, name='inicio'),
    
    # registro
     
    path('registro/', views.registro, name='registro'),
    
    # crud completo
    
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('  editar_usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    
    # login
    
    path('valida_login/',valida_login, name='valida_login'),
] 
=======
    path('index/', views.index, name='index'), 
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('form_editar_usuario/', views.form_editar_usuario, name='form_editar_usuario'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),
] 

>>>>>>> c348d75c42ef95f039be2ec4ebdc54f9761d9a36

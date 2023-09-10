

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
from proyecto.views import registro
from proyecto.views import inicio
from . import views  # Importa las vistas desde la aplicación app1
from proyecto.views import valida_login


urlpatterns = [
    
    
    path('admin/', admin.site.urls),
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
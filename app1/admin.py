from django.contrib import admin

from app1.models import Usuarios,Empleados

admin.site.register([Usuarios,Empleados])
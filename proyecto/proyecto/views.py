from datetime import datetime
from django.http import HttpResponse  
from django.template  import Template,context
import datetime
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required



@login_required

def index(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} cargado exitosamente !!!')
        else:
            messages.error(request, 'Usuario no cargado !!!')
    else:
        form = UserChangeForm()
    
    context = {'form': form}
    return render(request, "index.html", context)


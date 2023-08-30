from datetime import datetime
from django.http import HttpResponse  
from django.template  import Template,context
import datetime
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
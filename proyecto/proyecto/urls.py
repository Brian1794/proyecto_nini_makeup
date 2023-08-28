from django.contrib import admin
from django.urls import path 
from app1 import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='homepage'),
    path('admin/', admin.site.urls),
]

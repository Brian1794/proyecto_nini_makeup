from django.contrib import admin
from django.urls import path 
from django.urls import path,include

from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
]

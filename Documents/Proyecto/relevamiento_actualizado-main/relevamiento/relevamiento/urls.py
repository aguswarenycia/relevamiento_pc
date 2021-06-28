"""relevamiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
#from farmacia import views
from farmacia.views import Inicio,ListarFcias#, Login, logout_request
#from .usuario.views import Login
# url farmacia:crear_farmacia 
from django.conf import settings
from django.conf.urls.static import static

# Librerias para login y logout
from django.contrib.auth import login,logout


urlpatterns = [
    path('admin/', admin.site.urls),#modelo vista template (similar a vista controlador)
    path('farmacias/', include(('farmacia.urls','farmacia'))),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Inicio.as_view(), name = 'index'),
    # path('login/', views.login_request, name = 'login'),
    # path('logout/', views.logout_request, name = 'logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

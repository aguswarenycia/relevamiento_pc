# es necesario el url patterns  #URL CRUD
#from relevamiento.farmacia.models import Provincia
from django.urls import path

from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
from .views import (
    #ActualizarProvAct,
    ActivarPrograma,
    ListarProvDesactivadas,
    ListarProgramas,
    AgregarPrograma,
    EliminarPrograma,
    Actualizarprograma,
    EliminarProv,
    ActualizarProv,
    CrearProv, 
    ListarProv,  
    ListarFcias,   
    ListarLoc,
    ListarProgDesactivados
)

urlpatterns = [
    #-------------------------------- LOGIN --------------------------------
    path('lista_localidades/', login_required(ListarLoc.as_view()), name ="lista_localidades"),

    #-------------------------- Ruteo de CRUD  Para Programas --------------------------
    path('lista_programas/',login_required(ListarProgramas.as_view()), name = 'lista_programas'),
    path('agregar_programas/',login_required(AgregarPrograma.as_view()), name = 'agregar_programas'),
    path('eliminar_programa/<int:pk>',login_required(EliminarPrograma.as_view()), name  = 'eliminar_programa'),
    path('actualizar_programa/<int:pk>',login_required(Actualizarprograma.as_view()), name  = 'actualizar_programa'),
    path('activar_programa/<int:pk>', login_required(ActivarPrograma.as_view()),name = 'activar_programa'),

    
    path('listar_provincias/', login_required(ListarProv.as_view()), name  = 'listar_provincias'),
    path('lista_prov_desactivadas/',login_required(ListarProvDesactivadas.as_view()),name = 'lista_prov_desactivadas'),
    path('agregar_prov/', CrearProv.as_view(), name  = 'agregar_prov'),
    path('eliminar_prov/<int:pk>', EliminarProv.as_view(), name  = 'eliminar_prov'),
    path('actualizar_prov/<int:pk>', ActualizarProv.as_view(), name  = 'actualizar_prov'),
    path('lista_farmacias/', login_required(ListarFcias.as_view()), name ="lista_farmacias"),
    path('lista_programas_desactivados/', login_required(ListarProgDesactivados.as_view()), name ="lista_programas_desactivados"),

] 
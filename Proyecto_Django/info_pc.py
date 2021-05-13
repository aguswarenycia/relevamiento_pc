#importar librerias

import socket #libreria para saber nombre del PC
import platform #libreria para obtener especificaciones de hardware
import urllib.request #libreria para obtener ip publica y privada
import psutil #libreria para el manejo de memoria
import winapps #libreria para manejo de aplicaciones de windows
from subprocess import Popen #libreria para ejecutar subprocesos de windows
# Importar las librerias del Sistema Operativo
from os import remove
from os import path

from io import open #libreria para manejo de archivos

#abrir el archivo con una variable global
archivo = open("info_pc.txt","w")
# abre el archivo con el nombre que se le indica en elk primer parametro en caso
# de que no exista entonces lo crea y en el segundo
# parametro se le indica como se quiere abrir el archivo a = add w = write, r = read


#Función para obtener el nombre de la maquina
def nombrePC():
    nombre_PC = socket.gethostname()
    archivo.write("Nombre de la PC: " + nombre_PC)

#Funcion para obtener las IP
def IPpriv():
    nombre_PC = socket.gethostname()
    IPpriv = socket.gethostbyname(nombre_PC)
    archivo.write("IP privada: " + IPpriv)

def IPpub():
    ip_externa = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    archivo.write("IP publica: " + ip_externa)



#funcion  que devuelve nformacion del sistema
def sist():
    arqui_sist=platform.architecture()
    archivo.write("Arquitectura y SO: " + str(arqui_sist))
    vers = platform.release()
    archivo.write("\nVersion: " + vers)

#Funcion que devuelve informacion sobre el hardware
def Cores():
    tipo_mauina=platform.machine()
    archivo.write("Tipo de maquina: " + tipo_mauina)
    procesador = platform.processor()
    archivo.write("\n" + "Procesador: " + procesador)
    cores_fisicos = psutil.cpu_count(logical=False)
    cores_totales = psutil.cpu_count(logical=True)
    archivo.write("\n" + "cores fisicos: " + str(cores_fisicos) + "\n" + "cores totales: " + str(cores_totales))

#funcion de convfersion de unidades de almacenamiento
"""
    Reescala los bytes al formato adecuado
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
"""
def get_size(bytes, sufijo="B"):
    factor_conversion = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor_conversion:
            return f"{bytes:.2f}{unidad}{sufijo}" #retorna la unidad de medida final redondeada a 2 decimales con su correspondiente abreviatura
        bytes /= factor_conversion

def memoriaRAM():
    ram = psutil.virtual_memory()
    archivo.write("\nMemoria RAM  total: " + get_size(ram.total))
    archivo.write("\nMemoria RAM usada: " + get_size(ram.used))
    archivo.write("\nMemoria RAM disponible: " + get_size(ram.available))


#funcion que devuelve el espacio en disco disponible

def espacioEnDisco():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        archivo.write(f"=== Disco Local: {partition.device} ===\n")
        archivo.write(f"Punto de montaje: {partition.mountpoint}\n")
        archivo.write(f"File system type: {partition.fstype}\n")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        archivo.write("Espacio total en disco: " + get_size(partition_usage.total))
        archivo.write("\nEspacio usado en disco: " + get_size(partition_usage.used))
        archivo.write("\nEspacio libre en disco: " + get_size(partition_usage.free) + "\n")
        archivo.write("-" * 50 + "\n")

#funcion que ejecuta al bat para obtener la id y guardarla en un txt
def get_id():
    p = Popen("get_id_any.bat")
    stdout, stderr = p.communicate()

# #funcion que concatena los txt generando un tercer archivo final y eliminando los anteriores
# def concatenar():
#     filenames = ['info_pc.txt', 'Any_id.txt']  
#     with open('info_final_pc.txt', 'w') as outfile:
      
#     # iterar sobre la lista
#         for names in filenames:
    
#             # abrir cada archivo en modo lectura
#             with open(names) as infile:
    
#                 # leer los datos del archivo_1 y el archivo_2
                
#                 outfile.write(infile.read())
    
#             # agregar '\n' para guardar los datos del archivo_2
#             outfile.write("\n")

#             if path.exists('info_pc.txt') and path.exists('Any_id.txt'):
#                 archivo.close()
#                 remove('info_pc.txt')
#                 remove('Any_id.txt')


def any_instalado():
    # obtiene una lista con cada aplicacion instalada en windows
    for item in winapps.list_installed():
        if item.name == "AnyDesk":
            archivo.write("Anydesk Instalado || ")
            get_id()# llamada a la funcion para obtener el id y guardarlo en un txt
            #concatenar()#llamada a la funcion que ejecuta la concatencacion del txt con especificaciones y la id del any
        else:
            continue
            archivo.write("AnyDesk NO instalado")



#Funcion que une a todas las anteriores y cierra el archivo
def EjecutarTodo():
    archivo.write("="*40 + "Nombre PC" + "="*40 + "\n")
    nombrePC()
    archivo.write("\n" + "="*40 + "Informacion IP" + "="*40 + "\n")
    IPpriv()
    archivo.write("\n")
    IPpub()
    archivo.write("\n" + "=" * 40 + "SISTEMA" + "=" * 40 + "\n")
    sist()
    archivo.write("\n" + "=" * 40 + "Hardware" + "=" * 40 + "\n")
    Cores()
    archivo.write("\n" + "=" * 40 + "Memoria RAM" + "=" * 40)
    memoriaRAM()
    archivo.write("\n" + "=" * 40 + "Memoria en Disco" + "=" * 40 + "\n")
    espacioEnDisco()
    
    archivo.write("\n" + "=" * 40 + "AnyDesk" + "=" * 40 + "\n")
    any_instalado()
    archivo.close() #CERRAR ARCHIVO SIEMPRE AL FINAL XD

EjecutarTodo()

#Concatenar los 2 archivos en uno solo
filenames = ['info_pc.txt', 'Any_id.txt']
with open('especificaciones.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

#eliminar los 2 archivos restantes
if path.exists('info_pc.txt') and path.exists('Any_id.txt'):
    remove('info_pc.txt')
    remove('Any_id.txt') 


#SCRIPT DE RELEVAMIENTO LISTO










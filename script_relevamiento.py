# Importar librerias

import socket #libreria para saber nombre del PC
import platform #libreria para obtener especificaciones de hardware
import urllib.request #libreria para obtener ip publica y privada
import psutil #libreria para el manejo de memoria
import winapps #libreria para manejo de aplicaciones de windows
from subprocess import Popen #libreria para ejecutar subprocesos de windows
# Importar las librerias del Sistema Operativo
from os import remove # libreria que permite borrar un archivo del sistema
from os import path # libreria que permite obtener la ruta de un archivo del sistema
from io import open # libreria para manejo de archivos de entrada y salida estandar

# Abrir el archivo con una variable global
archivo = open("info_pc.txt","w")
# abre el archivo con el nombre que se le indica en elk primer parametro en caso
# de que no exista entonces lo crea y en el segundo
# parametro se le indica como se quiere abrir el archivo a = add w = write, r = read

# Función para obtener el nombre de la maquina
def nombrePC():
    nombre_PC = socket.gethostname()
    archivo.write("Nombre de la PC: " + nombre_PC)

# Funcion para obtener las IP
def IPpriv():
    nombre_PC = socket.gethostname()
    IPpriv = socket.gethostbyname(nombre_PC)
    archivo.write("IP privada: " + IPpriv)

def IPpub():
    ip_externa = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    archivo.write("IP publica: " + ip_externa)

# Función  que devuelve nformacion del sistema
def sist():
    arqui_sist=platform.architecture()
    archivo.write("Arquitectura y SO: " + str(arqui_sist))
    vers = platform.release()
    archivo.write("\nVersion: " + vers)

# Funcion que devuelve informacion sobre el hardware
def Cores():
    tipo_mauina=platform.machine()
    archivo.write("Tipo de maquina: " + tipo_mauina)
    procesador = platform.processor()
    archivo.write("\n" + "Procesador: " + procesador)
    cores_fisicos = psutil.cpu_count(logical=False)
    cores_totales = psutil.cpu_count(logical=True)
    archivo.write("\n" + "cores fisicos: " + str(cores_fisicos) + "\n" + "cores totales: " + str(cores_totales))

# Funcion de convfersion de unidades de almacenamiento
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

"""
Consultar mejora, en esta parte se puede retornar un mensaje de "estado crítico en caso de que el porcentaje de 
memoria ram ocupado sea mayor o igual a 90%
"""

def memoriaRAM():
    ram = psutil.virtual_memory()
    archivo.write("\nMemoria RAM  total: " + get_size(ram.total))
    archivo.write("\nMemoria RAM usada: " + get_size(ram.used))
    archivo.write("\nMemoria RAM disponible: " + get_size(ram.available))
    # print(f"Percentage: {swap.percent}%")
    archivo.write("\nPorcentage de memoria ram usado: " + str(ram.percent) + "%")

# Funcion que devuelve el espacio en disco disponible

"""
Consultar mejora, en esta parte se puede retornar un mensaje de "estado crítico en caso de que el porcentaje de 
memoria ocupado sea mayor o igual a 90%
"""
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
        archivo.write("\nEspacio libre en disco: " + get_size(partition_usage.free))
        # print(f"  Percentage: {partition_usage.percent}%")
        archivo.write("\nProcentage de espacio utilizado: " + str(partition_usage.percent) + "%\n")
        
        archivo.write("-" * 50 + "\n")

# Funcion que ejecuta al bat para obtener la id y guardarla en un txt
def get_id():
    p = Popen("get_id_any.bat")
    stdout, stderr = p.communicate()

# Función que devuelve una lista y filtra para verificar que el any_desk esté instalado
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


# Funcion que  recorre la lista de programas instalados e imprime en pantalla 

"""
Consultar si a esta funcion se le puede hacer una mejora: por ejemplo tener una lista 
(o 2 listas, una de 64 y otra de 32 bits) predefinida como constante 
donde se compare con la lista generada por winnapps para saber si tiene programas de mas o le faltan algunos.

* Retrono de la funcion en cada uno de los posibles casos

- En caso de que tenga programas de más: devolver la lista con los nombres de tales programas y fecha de instalación
  con  un mensaje que indique que deben ser desinstalados o consultar a sistemas para mantenerlos instalados 

- En caso de le falte programas: devolver una lista con los nombres de los programas faltanttes e indicar un mensaje 
  que indique priorizar la instalación de los mismos

- En caso de tener los programas justos y necesarios se debe retornal la lista con sus nombres e indicar que todo está
  en orden
"""

def mostrar_programas():
    
    # Creacion de un archivo de texto para almacenar todos los programas instalados
    archivo_programas = open("programas_instalados.txt","w")
    
    # Grabar en el archivo un título indicando el nombre de la PC
    archivo_programas.write("\n" + "=" * 40 + "Programas instalados en " + socket.gethostname() + "=" * 40 + "\n")
    # loop que recorre la lista de programas instalados 
    for item in winapps.list_installed():
        # Grabacion en el achivo de texto de los programas instalados

        if item.install_date == None:
            archivo_programas.write(item.name + " - Fecha de instalacion: de Fabrica o instalado por sistemas" + "\n")
        else:
            archivo_programas.write(item.name + " - Fecha de instalacion: " + str(item.install_date) + "\n")
    # Cierre del archivo con los programas instalados
    archivo_programas.close()

# Funcion que une a todas las anteriores y cierra el archivo
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

    mostrar_programas()

EjecutarTodo()

# Concatenar los 2 archivos en uno solo
filenames = ['info_pc.txt', 'Any_id.txt']
with open('especificaciones.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

# Eliminar los 2 archivos restantes
if path.exists('info_pc.txt') and path.exists('Any_id.txt'):
    remove('info_pc.txt')
    remove('Any_id.txt') 

# SCRIPT DE RELEVAMIENTO LISTO

""" 
generar en la base de datos una tabla con los programas que se necesita para cada sector
y asi poder compararla con la lista generada por el script 
"""
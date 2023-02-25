import msvcrt
import os
import re
def continuar ():
    print("Presione c para continuar...")
    key = None
    while key != 'c':
        key = msvcrt.getwch()
    os.system ("cls")

def carga(doc):
     print("------------------INGRESE RUTA DEL ARCHIVO--------------------")
     documeto = str(doc)
     archivo = open(documeto, "r") 
     print("Archivo cargado satisfactoriamente")

def mostar (pos):
    lista = []
    print("------------------INGRESE RUTA DEL ARCHIVO--------------------")
    doc = str(input())
    archivo = open(doc, "r")
    with archivo as doc:
     next(doc, None)
     for line in doc:
         lista = line.split(";")
         mostrar = lista[pos]
         print(mostrar)

def buscar (nombre):
  print("------------------INGRESE RUTA DEL ARCHIVO--------------------")
  doc = str(input())
  man = open(doc)
  for linea in man:
     linea = linea.rstrip()
     if re.search(nombre, linea):
        lista = []
        lista = linea.split(";")
        mostrar = lista[0]
        print(mostrar)

def buscara (aaa):
 print("------------------INGRESE RUTA DEL ARCHIVO--------------------")
 doc = str(input())
 man = open(doc)
 for linea in man:
     linea = linea.rstrip()
     if re.search(aaa, linea):
        lista = []
        lista = linea.split(";")
        mostrar = lista[0]+" GENERO "+lista[3]
        print(mostrar)


def gestion():
                opg = '0'
                while not(opg =='3'):
                    print("------------------------")
                    print(' 1. MOSTRAR PELICULAS')
                    print(' 2. MOSTRAR ACTORES')
                    print(' 3. REGRESAR AL MENÚ PRINCIPAL')
                    opcion = input('  --- INGRESE UNA OPCION --- ')
                    if (opcion=='1'):
                        print(' **** MOSTAR PELICULAS ****')
                        mostar(0)

                    elif (opcion=='2'):
                        print(' **** MOSTAR ACTORES ****')
                        mostar(1)
                    elif (opcion == '3'):
                        break
                    else:
                        print('No existe la opcion')

def filtrado():
                opg = '0'
                while not(opg =='3'):
                    print("------------------------")
                    print(' 1. FILTRAR POR ACTOR')
                    print(' 2. FILTRAR POR AÑO')
                    print(' 3. FILTRAR POR GENERO')
                    print(' 4. REGRESAR AL MENÚ PRINCIPAL')
                    opcion = input('  --- INGRESE UNA OPCION --- ')
                    if (opcion=='1'):
                        nom = input("INGRESE EL NOMBRE QUE DESEA BUSCAR ")
                        print(' **** PELICULAS EN LAS QUE PARTICIPA ****')
                        buscar (nom)

                    elif (opcion=='2'):
                        ano = input("INGRESE EL AÑO QUE DESEA BUSCAR ")
                        print(' **** PELICULAS DEL AÑO ****')
                        buscara(ano)
                    
                    elif (opcion =='3'):
                        nom = input("INGRESE EL GENREO QUE DESEA BUSCAR ")
                        print(' **** PELICULAS DEL GENERO ****')
                        buscar(nom)    

                    elif (opcion == '4'):
                        break
                    else:
                        print('No existe la opcion')

def grafica():
                pass

def salir ():
                print("--------------GRACIAS POR USAR MI PROGRAMA------------")
                os.system("exit")
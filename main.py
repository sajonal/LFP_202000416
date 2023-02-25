import msvcrt
import os
from funciones import *
print("---------------------------------------")
print("LENGUAJES FORMALES Y DE PROGRAMACION  ")
print("SECCION: A+")
print("CARNE: 202000416")
print("NOMBRE: JONATHAN EDUARDO SANTOS LETONA")
print("---------------------------------------")

continuar()

print("----------------MENU PRINCIPAL-------------------------")
opcion = '0'
while not(opcion =='5'):
    print("------------------------")
    print(' 1. CARGA DE ARCHIVO')
    print(' 2. GESTIONAR PELICULAS')
    print(' 3. FILTRADO')
    print(' 4.GRAFICA')
    print(' 5. SALIR')

    opcion = input('  --- INGRESE UNA OPCION --- ')
    if (opcion=='1'):
        print(' **** CARGA DE ARCHIVO ****')
        print("------------------INGRESE RUTA DEL ARCHIVO--------------------")
        doc = str(input())
        carga(doc)
    elif (opcion=='2'):
        print(' **** GESTIONAR PELICULAS ****')
        gestion()
    elif (opcion=='3'):
        print(' **** FILTRADO ****')
        filtrado()
    elif (opcion=='4'):
        print(' **** GRAFICA ****')
        grafica()
    elif (opcion=='5'):
        salir()
    else:
        print('No existe la opcion')


    
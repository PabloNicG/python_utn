import numpy as np
import random

#Ejercicio1

#Ingresar un numero por consola y mostrar su tabla de multiplicacion

#Declaro la matriz
matriz = []

#Declaro una variable a la cual le voy a asignar el numero ingresado 
x = int(input("Ingrese el numero que quiere multiplicar: "))
print("La tabla de multiplicacion de: ", x)

#Declaro un bucle for, con un rango de 10 posiciones
# 0 - 9 
for i in range(10):
    matriz.append((i+1)*x)
    print(x, " x ", i+1," = ", matriz[i])
    
    #En este paso con la funcion 'append' agrego un elemento al final de la lista
    #Y en el mismo lugar desarrollo la logica, para que comience desde el 1 y no desde el 0 
    #le sumo 1 a la posicion i y luego lo multiplico por X (recordemos que x será el numero que
    # ingrese por consola).
    # #Luego muestro por pantalla
    
'''
El tipo de dato 'range' es una lista inmutable de numeros (anteriormente era una funcion),
es una sucesion de numeros, empieza en 0 y termina en n-1. 

'''





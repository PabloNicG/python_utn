import numpy as np
import random
#Ejercicio2

''' Llenar dos arreglos de dimension 5 con numeros enteros. Sumar los elementos
de la misma posicion y almacenar los resultados en un tercer arreglo y mostrarlo
en pantalla '''

n = 5
m = 5
c = 5

matriz1 = []
matriz2 = []

for j in range(c):
    matriz1.append([])
    matriz2.append([])

for x in range(n):
    matriz1[j].append(random.randrange(10))

for i in range(m):
    matriz2[x].append(random.randrange(10))
    

print("Matriz1:", matriz1[j])
print("Matriz2:", matriz2[x])

matriz3 = list(map(lambda x,y: x+y,matriz1[j],matriz2[x]))
print("Matriz3:",matriz3)

import numpy as np
import random
#Ejercicio2

''' Llenar dos arreglos de dimension 5 con numeros enteros. Sumar los elementos
de la misma posicion y almacenar los resultados en un tercer arreglo y mostrarlo
en pantalla '''

#Declaro  las variables que contendran la dimension de nuestros arreglos
n = 5
m = 5
c = 5

#Declaro los arreglos que conforman nuestra matriz 
matriz1 = []
matriz2 = []


#Declaro un bucle for para inicializar los arreglos 
for j in range(c):
    matriz1.append([])
    matriz2.append([])

#Los siguientes bucles contendran nuestros arreglos dandole valores aleatorios entre 0 y 10 
for x in range(n):
    matriz1[j].append(random.randrange(10))

for i in range(m):
    matriz2[x].append(random.randrange(10))
    

#Muestro el contenido
print("Matriz1:", matriz1[j])
print("Matriz2:", matriz2[x])

#Declaro un tercer arreglo donde guardare el resultado de la suma de los dos primeros arreglos 
matriz3 = list(map(lambda x,y: x+y,matriz1[j],matriz2[x]))
print("Matriz3:",matriz3)


'''
Explicacion de la funcion 'map' y 'lambda'

La función map() toma una función y una lista y aplica esa función a cada elemento de esa lista, 
produciendo una nueva lista.
Esta función trabaja de una forma muy similar a filter(), con la diferencia que en lugar de aplicar 
una condición a un elemento de una lista o secuencia, aplica una función sobre todos los elementos 
y como resultado se devuelve un lista de números.

En nuestro caso utilizamos la funcion lambda para sumar dos arreglos y guardar el resultado en otro.

https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion5/funciones_orden_superior.html
'''
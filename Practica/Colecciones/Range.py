'''
Una lista es un conjunto ordenado de elementos del mismo tipo o diferente tipo, su contenido
puede ser modificado. Dentro de estas se encuentra el tipo Range, este tipo de dato es una 
lista inmutable (a diferencia de la lista) de numeros enteros, es una sucesion de numeros.

Anteriormente en versiones de python se consideraba una funcion, pero a partir de la version 3 
es un tipo de dato, pero se utiliza como funcion.

Este tipo se puede representar con uno, o varios argumentos, este va desde el 0 hasta el n-1 y
para poder acceder a sus valores hay que convertirlo en una lista. Range solo admite valores enteros.
'''

# m: el valor inicial
# n: el valor final (que no se alcanza nunca)
# p: el paso (la cantidad que se avanza cada vez).

#Declaro una variable un range de tamaño 10
R = range(10)

#Convierto en lista
list(R)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(8))
#[0, 1, 2, 3, 4, 5, 6, 7]

'''
El tipo range con mas de un argumento trabaja con renge(m,n) y crea una lista de numeros
consecutivos que comienzan en m y terminan en n-1
'''

list(range(3,8))
#[3, 4, 5, 6, 7]

list(range(-8,3))
#[-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2]

'''
Con tres argumentos range(m,n,p) crea una lista de numeros, empieza en m, y termina antes de igualar
o superar a n, el tercer argumento sirve para aumentar los numeros. Por ej: de dos en dos 
** p nunca puede tener el valor de 0 **
'''
# ---------m, n, p
list(range(5,20,3))
#[5, 8, 11, 14, 17] muestra el primer numero, suma 3 y hasta el siguiente y así sucesivamente hasta llegar a n

'''
Este tipo de dato no se puede concatenar libremente, siempre hay que convertirlo en una lista.
'''

# MAL! range(3) + range(7)

# BIEN! list(range(3)) + list(range(7))

list(range(3)) + list(range(7))
#[0, 1, 2, 0, 1, 2, 3, 4, 5, 6]

#Otra forma de concatenar

list(range(1,5)) + list(range(4,9))
#[1, 2, 3, 4, 4, 5, 6, 7, 8]

#Recorrer una secuencia

for i in range(1,11):
    print (i)
'''
1
2
3
4
5
6
7
8
9
10
'''


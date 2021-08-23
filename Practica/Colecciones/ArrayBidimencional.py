import numpy as np
import random

''' 
Array bidimencional con datos random

Utilizaremos la biblioteca  numpy 
'''

#Declaro las filas y las columnas con datos de tamaño ya establecidos
n=3
m=3

#Declaro mi matriz
matrix=[]

#Declaro el bucle for para el tamaño n
for i in range(n):
    matrix.append([])

#Blucle for para el tamaño m
    for j in range(m):
        matrix[i].append(random.randrange(0,10))
        #append agrega un elemento al final de la lista.
        #En cada iteracion la matriz obtendrá un valor aleatorio en el rando especificado
        #La matriz será llenada de numeros random. Randrage devuele numeros random dentro del rango especificado


print (matrix, end=' ')
print(matrix.count(3))
''' 
Como primera instancia creo la matriz, luego por teclado pido cantidad de filas y columnas
luego comienzo a declarar los bucles en este caso 'for' que será quien me haga la iteracion
de los elementos.  
'''
#Declarada como lista vacia 
matriz = []

#Pedido de tamaño de matriz

filas = int(input("Cantidad de filas: "))
columnas = int(input("Cantidad de columnas: "))
print('\n')

#Agrego elementos a la lista - la matriz va a ser de tantas filas como columnas sean agregadas
for i in range(filas):
    matriz.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input("Elemento: [%d|%d] : " % (f,c)))
        #Pido por consola los numeros que quiera ingresar el usuario
print (matriz, end=' ')


'''
Otra forma de realizar arrays bidimencionales. 
Utilizacion de map y lambda
'''

a = [1,2,3,4,5];
b = [5,4,3,2,1];

c = list(map(lambda x,y : x + y, a,b))

print("Resultado Suma: ",c)

c = list(map(lambda x,y : x - y, a,b))

print("Resultado Resa: ",c)

c = list(map(lambda x,y : x * y, a,b))

print("Resultado Multiplicacion: ",c)

c = list(map(lambda x,y : x / y, a,b))

print("Resultado Division: ",c)

'''
Otra forma de crear una matriz aleatoria es con la funcion random de 'np'
y randint
'''

n = 3
m = 3

'''
Dentro de randint se coloca el rango de numeros que quiero, en este caso 
entre 0 y 20, ademas se coloca el tamaño de la matriz con un size=(n,m).

Randint devuelve un numero entero entre un rango especificado
'''
matriz = np.random.randint(0,20, size=(5,5))
print(matriz)

#Forma con entrada de datos de tamaño por consola

n = int(input("Seleccione el tamaño de la matriz"))
m = int(input("Seleccione el tamaño de la matriz"))

matriz = np.random.randint(0,20, size=(n,m))

print(matriz)
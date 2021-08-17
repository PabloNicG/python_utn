#Definir una tupla

frutas = ("Naranja", "Manazana", "Mandarina")

# Tamaño de una tupla

print(len(frutas))

# Buscar por elemento (indice)

print(frutas[1])

# Buscar por elemento a la inversa

print(frutas[-1])

# Rango de valores

print(frutas[0:1])

# Recorrer elementos de una tupla

for fruta in frutas:
    #Para que no salga el salto de linea lo que se hace
    #es poner el modificador end=" " con un espacio
    #por defecto print lleva un salto de linea para
    #todos sus elementos "\n"
    print(fruta, end=" ")

"""
Si bien una tupla es inmutable existe una forma de modificarla, esto se  hace convirtiendo la
tupla a una lista, modificar el contenido y volver la lista a una tupla nuevamente
"""

#Creo una lista y le paso el tipo list a la tupla
frutaLista = list(frutas)
#Reemplazo un elemento
frutaLista[1] = "Melon"
#Convierto la lista frutaLista en una tupla nuevamente
fruta = tuple(frutaLista)
print('\n', fruta)

#para eliminar la tupla por completo
# del fruta



""" 
-----------------------------------------------------------------------------------
Método || Descripción
-----------------------------------------------------------------------------------
* index(elemento)  ||	Obtiene el índice de la primera ocurrencia del elemento en la tupla. 
                   ||  Si el elemento no se encuentra, se lanza la excepción ValueError.
-----------------------------------------------------------------------------------
* count(elemento)  ||  Devuelve el número de ocurrencias del elemento en la tupla.
-----------------------------------------------------------------------------------
"""
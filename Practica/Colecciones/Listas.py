lista = ["Pablo","David","Juan","Maria","Adrian"]

# Longitud de la lista
print(len(lista[2]))

# Append inserta un elemento al final de la lista
lista.append('Sandro')

# Insert agrega un elemento en el indice que indiquemos
lista.insert(1,'Juan Carlos')

# Remove elimina un elemento de la lista que indiquemos
lista.remove("David")

# Pop remueve el ultimo elemento agregado a la lista
#lista.pop()

# Para eliminar un indice
#del lista[0]

# Limpiar la lista de todos los elementos per no la elimina
#lista.clear()

# Borra completamente la lista
#del lista

print("Pablo" in lista)

#Ordenar elementos de una lista
lista.sort()
print(lista)
"""

-------------------------------------------------------------------------------------------------------
Método	  ||  Descripción
-------------------------------------------------------------------------------------------------------
* append() || Añade un nuevo elemento al final de la lista.
-------------------------------------------------------------------------------------------------------
* extend() || Añade un grupo de elementos (iterables) al final de la lista.
-------------------------------------------------------------------------------------------------------
* insert(indice, elemento) || Inserta un elemento en una posición concreta de la lista.
-------------------------------------------------------------------------------------------------------
* remove(elemento) || Elimina la primera ocurrencia del elemento en la lista.
-------------------------------------------------------------------------------------------------------
* pop([i])  || Obtiene y elimina el elemento de la lista en la posición i. 
            || Si no se especifica, obtiene y elimina el último elemento.
-------------------------------------------------------------------------------------------------------
* clear()	  || Borra todos los elementos de la lista.
-------------------------------------------------------------------------------------------------------
* index(elemento)  || Obtiene el índice de la primera ocurrencia del elemento en la lista. 
                   || Si el elemento no se encuentra, se lanza la excepción ValueError.
-------------------------------------------------------------------------------------------------------
* count(elemento)  ||	Devuelve el número de ocurrencias del elemento en la lista.
-------------------------------------------------------------------------------------------------------
* sort() || Ordena los elementos de la lista utilizando el operador <.
-------------------------------------------------------------------------------------------------------
* reverse()	|| Obtiene los elementos de la lista en orden inverso.
-------------------------------------------------------------------------------------------------------
* copy() || Devuelve una copia poco profunda de la lista.
-------------------------------------------------------------------------------------------------------

"""
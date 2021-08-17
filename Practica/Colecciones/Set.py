
"""
El Set en python es un tipo de lista que no contiene indice, no guarda posiciones y cada vez que se ejecuta cambia
de lugar los valores, comparte algunas funciones con las lista como puede ser len (Longitud)
"""

frutas = {"Manzana", "Banana", "Pera"}

print("Pera" in frutas)


# Agregar un elemento

frutas.add("Melon")
print(frutas)

#Remover un elemento

frutas.remove("Pera")
print(frutas)

#Tambien se podria utilizar "discard" para eliminar, la diferencia es que no da error
frutas.discard("Pera")
print(frutas)

#Para limpiar completamente el set
frutas.clear()
print(frutas)

#Para eliminar completamente el set se usa del
del frutas
print(frutas)


""" 
-----------------------------------------------------------------------------------
Método || Descripción
-----------------------------------------------------------------------------------
* add(e)	Añade un elemento al conjunto.
-----------------------------------------------------------------------------------
* clear() || Elimina todos los elementos del conjunto.
-----------------------------------------------------------------------------------
* copy() || Devuelve una copia superficial del conjunto.
-----------------------------------------------------------------------------------
* discard(e) || Elimina, si existe, el elemento del conjunto.
-----------------------------------------------------------------------------------
* pop() || Obtiene y elimina un elemento de forma aleatoria del conjunto.
-----------------------------------------------------------------------------------
* remove(e) || Elimina el elemento del conjunto. Si no existe lanza un error.
-----------------------------------------------------------------------------------
"""
"""
En los diccionarios se maneja como los de la vida real con una llave (key) y un valor (value) - Key:value
Diccionario no contiene indice, pero declarando llave se puede acceder
"""

diccionario = {
    'IDE':'Integrated Development Environment',
    'OPP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)

#Longitud
print(len(diccionario))

#Acceder a elemento
print(diccionario['IDE'])

#Otra forma
print(diccionario.get('OPP'))

#Modificando un diccionario

diccionario['DBMS'] = "dbms"
print(diccionario)

#Recorrer elementos con un for

for termino in diccionario:
    print(termino)

#Recorrer elementos con llave y valor, es necesario una funcion

for termino, valor in diccionario.items():
    print(termino, valor)
    #De esta forma puedo recorrer todos los elementos e imprimirlos
    
#Recuperar solamente las llaves
for termino in diccionario.keys():
    print(termino)

#Recuperar solamente los valores
for valor in diccionario.values():
    print(valor)

#Comprobar existencia de un elemento (respetar mayusculas o minusculas)
print("IDE" in diccionario)

#Agregar elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Remover elemento
diccionario.pop("DBMS")
print(diccionario)

#Limpiar de todos los elementos
#diccionario.clear()

#Eliminar la variable completa
#del diccionario


""" 
-----------------------------------------------------------------------------------
Método || Descripción
-----------------------------------------------------------------------------------
* clear()|| Elimina todos los elementos del diccionario.
-----------------------------------------------------------------------------------
* copy() || Devuelve una copia poco profunda del diccionario.
-----------------------------------------------------------------------------------
* get(clave[, valor]) || Devuelve el valor de la clave. 
                      || Si no existe, devuelve el valor valor si se indica y si no, None.
-----------------------------------------------------------------------------------
* items() || Devuelve una vista de los pares clave: valor del diccionario.
-----------------------------------------------------------------------------------
* keys() || Devuelve una vista de las claves del diccionario.
-----------------------------------------------------------------------------------
* pop(clave[, valor]) || Devuelve el valor del elemento cuya clave es clave y elimina el elemento del diccionario. 
                      || Si la clave no se encuentra, devuelve valor si se proporciona. 
                      || Si la clave no se encuentra y no se indica valor, lanza la excepción KeyError.
-----------------------------------------------------------------------------------
* setdefault(clave[, valor]) || Si la clave está en el diccionario, devuelve su valor. 
                             || Si no lo está, inserta la clave con el valor valor y lo 
                             || devuelve (si no se especifica valor, por defecto es None).
-----------------------------------------------------------------------------------
* values() || Devuelve una vista de los valores del diccionario.
-----------------------------------------------------------------------------------
"""


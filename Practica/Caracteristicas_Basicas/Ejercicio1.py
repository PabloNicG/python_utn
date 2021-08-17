"""
Declaracíon de Variables

# Podemos referenciar el tipo de dato o "hint" para saber que dato será
# No significa que solo almacenará el tipo, en python las variables pueden
# tener cualquier tipo de dato como un entero, solo es una practica para 
# referenciar

Las variables se mostraran en pantalla con la funcion 'print()'
"""
nombre: str = "Pablo"
apellido: str = "García"
edad: int = 27
altura: float = 1.75

print(nombre)
print(apellido)
print(edad)
print(altura)

# Si quisiera saber que tipó de  dato trae una variable utilizo la 
# funcion  'type()' dentro del print 

direccion = "La Plata"
print(direccion)
print(type(direccion))

"""
Cadenas 
"""

miAuto = "Ford" + "Focus"

print("Mi auto es: " + miAuto)

"""
Como podemos observar una cadena es unida por un '+' en esta variable
"""
#Recomiendo

miAuto1 = "Ford"
modelo = "Focus"

print("Mi auto es : " + miAuto1 + " " + modelo)

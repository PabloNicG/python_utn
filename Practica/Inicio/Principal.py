"""
INTRODUCCION A PYTHON A

-------------
Bibliografía:

Link:  https://ingsosa.com/tipos-de-datos-en-python/
Link:  https://j2logo.com/python/tutorial/


-------------

--La forma para comentar en python es utilizando triple comilla doble.

--La funcion print() es la que me permitira mostrar en pantalla un mensaje
funciona de la misma forma que System.out.println() o console.log()
"""

print("Hola mundo con Python ")

"""
Declaración de variables
 -- Python se ejecuta desde arriba hacía abajo
"""

miVariable = "Hola a todos!"

print(miVariable)

print("------------------------------------")

#Para destacar otra forma de mostrtar las variables es ingresando una f delante de la
#cadena de texto y con llaves {} se puede incluir las variables

variable = " VARIABLE"
print(f'Nueva forma de inmprimir una {variable}')

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

#En python existe el NONE que sería lo mismo que Null en Java

miVariable1 = None
#De esta forma indicamos que una variable es nula, no tiene contenido


# Si quisiera saber que tipó de  dato trae una variable utilizo la 
# funcion  'type()' dentro del print 

direccion = "La Plata"
print(direccion)
print(type(direccion))

"""
Operaciones simples

"""
num1 = 1
num2 = 2

#suma
suma = num1 + num2
print(suma)

#resta
resta = num1 - num2
print(resta)

#multiplicacion
multiplicacion = num1 * num2
print(multiplicacion)

#division
division = num1 / num2
print(division)

# residuo %
residuo = num1 % num2

print(f'Resultado residuo de una division: {residuo}')


# exponente

exponente = num1 ** num2
print(f'Resultado exponente: {exponente}')


##Otra forma de hacerlas es

print("Suma: ", num1 + num2)

##

n1 = "1"
n2 = "2"

print("Conversion:", int(n1) + int(n2))

"""
Tipos de datos en Python 

-- Entero - int
-- Decimal - float
-- Caracter - chr
-- Cadena de texto - str
-- Booleano - bool

int = 40
float = 14.3
chr = 'o'
str = "Hola mundo"
bool = False
 -- En caso de los valores booleanos corresponde el valor True = 1  y False = 0

--Convierto numeros decimales y booleanos con la funcion (int)
"""
pi = 3.14
esDeDia = False

print(int(pi))
print(int(esDeDia))

"""
--Convierto numero enteros y booleanos a Decimal (float)
"""
numero1 = 10
esDeNoche = True

print(float(numero1))
print(float(esDeNoche))

"""
--Convierto en cadena de texto cualquier tipo de dato con (str)
"""
pi = 3.14
numero1 = 10
esDeNoche = True

print(str(pi))
print(str(numero1))
print(str(esDeNoche))

"""
Listas 

--Las listas en Python son los comunmente llamados Arrays, estas listas
se pueden modificar, eliminar y agregar elementos. Las mismas mantienen 
el formato de array empezando en el indice "0" hasta "n"
"""

#Definicion de una lista

lista1 = [1,2,3,4,5]

print(lista1)

#Imprimimos el primer elemento de la lista
print(lista1[0])

#Modificando una elemento
 #En este caso modificamos el segundo elemento o tercer elemento por indice [2]
lista1[2] = 33
print(lista1)

#Sublistas
sublista = lista1[1:4]
print(lista1)
print(sublista)
print(lista1 [:-1])

"""
Tuplas
-- Las tuplas son listas de elementos estaticos, no se pueden modificar
se representan dentro de parentesis 
"""

tupla1 = (1,3,4,5,6)
print(tupla1)
print(tupla1[0])
print(tupla1[3])

"""
Diccionarios
--Cada elemento se compone de clave-valor, se encierran entre llaves
se puede acceder al valor usando la clave pero no se puede al reves,
estos mismos se pueden modificar, agregar y eliminar
"""

diccionario1 = {"Codigo": 1234, "Materia": "Metodologia de Sistemas I", "Profesor" : "A.Cortez"}
print(diccionario1)

#Para llegar a un valor vamos a utilizar el indice o clave para poder acceder a ella
print(diccionario1["Profesor"])
print(diccionario1["Materia"])

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



"""
Operadores Aritmeticos
------------------------------------------------------------------------
OPERADOR   || DESCRIPCIÓN	USO
------------------------------------------------------------------------
+	Realiza|| Adición entre los operandos	     || 12 + 3 = 15
------------------------------------------------------------------------
-	Realiza|| Substracción entre los operandos	 || 12 - 3 = 9
------------------------------------------------------------------------
*	Realiza|| Multiplicación entre los operandos ||	12 * 3 = 36
------------------------------------------------------------------------
/	Realiza|| División entre los operandos   	 || 12 / 3 = 4
------------------------------------------------------------------------
%	Realiza|| un módulo entre los operandos	     || 16 % 3 = 1
------------------------------------------------------------------------
**	Realiza|| la potencia de los operandos	     || 12 ** 3 = 1728
------------------------------------------------------------------------
//	Realiza|| la división con resultado de número entero || 18 // 5 = 3
------------------------------------------------------------------------



Operadores Relacionales
--------------------------------------------------------------------------------------------------------------------------
OPERADOR	DESCRIPCIÓN	                                                                    USO
--------------------------------------------------------------------------------------------------------------------------
>	|| Devuelve True si el operador de la izquierda es mayor que el operador de la derecha	|| 12 > 3 devuelve True
--------------------------------------------------------------------------------------------------------------------------
<	|| Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	|| 12 < 3 devuelve False
--------------------------------------------------------------------------------------------------------------------------
==	|| Devuelve True si ambos operandos son iguales                                         || 12 == 3 devuelve False
--------------------------------------------------------------------------------------------------------------------------
>=	|| Devuelve True si el operador de la izquierda es mayor o igual que el operador de     ||
    || la derecha                                                                           || 12 >= 3 devuelve True
--------------------------------------------------------------------------------------------------------------------------
<=	|| Devuelve True si el operador de la derecha es mayor o igual que el operador de       ||
    || la izquierda	                                                                        ||    12 <= 3 devuelve False
--------------------------------------------------------------------------
!=	|| Devuelve True si ambos operandos no son iguales
--------------------------------------------------------------------------------------------------------------------------




Operadores de Asignacion
--------------------------------------------------------------------------
OPERADOR	DESCRIPCIÓN
--------------------------------------------------------------------------
=	      ||  a = 5. El valor 5 es asignado a la variable a
--------------------------------------------------------------------------
+=	      ||  a += 5 es equivalente a a = a + 5
--------------------------------------------------------------------------
-=	      ||  a -= 5 es equivalente a a = a - 5
--------------------------------------------------------------------------
*=	      ||  a *= 3 es equivalente a a = a * 3
--------------------------------------------------------------------------
/=	      ||  a /= 3 es equivalente a a = a / 3
--------------------------------------------------------------------------
%=	      ||  a %= 3 es equivalente a a = a % 3
--------------------------------------------------------------------------
**=	      ||  a **= 3 es equivalente a a = a ** 3
--------------------------------------------------------------------------
//=	a     ||  //= 3 es equivalente a a = a // 3
--------------------------------------------------------------------------
&=	      ||  a &= 3 es equivalente a a = a & 3
--------------------------------------------------------------------------
|=	      ||  a |= 3 es equivalente a a = a | 3
--------------------------------------------------------------------------
^=	      ||  a ^= 3 es equivalente a a = a ^ 3
--------------------------------------------------------------------------
>>=	      ||  a >>= 3 es equivalente a a = a >> 3
--------------------------------------------------------------------------
<<=	      ||  a <<= 3 es equivalente a a = a << 3
--------------------------------------------------------------------------



Operadores Logicos
--------------------------------------------------------------------------
OPERADOR  || DESCRIPCIÓN	                                    ||  USO
--------------------------------------------------------------------------
and	      || Devuelve True si ambos operandos son True          ||a and b
or	      || Devuelve True si alguno de los operandos es True	||a or b
not       || Devuelve True si alguno de los operandos False	    ||not a


"""

"""
Ingreso de datos

-- El ingreso de datos lo vamos a realizar con la funcion 'Input()'

"""

# Funcion Input -- Nos permite ingresar valores a una variable

resultado  = input('Ingresa tu edad: ')

print("La edad es:", resultado)

print("Fin del programa")
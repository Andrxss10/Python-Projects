# ----- *ARGS y **KWARGS -----
""" Utilizamos *args y **kwargs para indicar que pasaremos un número
indefinido de argumentos(*args) y argumentos de clave y valor(**kwargs) en una
función. No es necesario poner el nombre args o kwargs lo que los diferencia
es el simbolo * y **, de nombre puede ir cualquier cosa."""

# ---- *ARGS ----
""" Pasamos un número indefinido de argumentos en una función """

#Creamos una función prueba y de argumentos ingresamos la cantidad
#de argumentos que queramos
def prueba(*args):
    valor = 0
    for i in args:
        valor += 1
        print(f"El argumento número {valor} es: {i}")
        
prueba("rojo","Verde","aMarillO",3)

#Podemos cambiar el nombre porque lo que lo diferencia es el *
def suma(*numeros):
    total_suma = 0
    for i in numeros:
        total_suma += i
    print(f"El valor total de la suma fue {total_suma}")

suma(1,2,3,4,5,6,7,8,9,10)


# ----- *KWARGS -----
""" Pasamos un número indefinido de argumentos en formato clave y valor """

#Se le pasa clave y valor como argumentos de forma indefinida
def claves(**kwargs):
    numero = 0
    for clave in kwargs.keys():
        numero += 1
        print(f"Clave {numero}: {clave}")

    numero = 0
    for value in kwargs.values():
        numero += 1
        print(f"Valor {numero}: {value}")

    print("\n")
    for clave, value in kwargs.items():
        print(f"{clave} = {value}")
    print("\n")
claves(nombre="Javier", apellidos="Gómez de la barca", edad=23)

#Puede imprimir recibir un diccionario(clave valor) entero como argumento
#pero al llamarla debemos poner tambi[en el **
def imprime_diccionario(**diccionario):
    for elemento in diccionario.items():
        print(elemento)

usuario1 = {"nombre": "Andrés", "apellido": "Ballen", "edad": 21}

imprime_diccionario(**usuario1)

print("\n")

# ----- Jerarquía de llamadas *ARGS Y **KWARGS -------

#Se pueden incluir argumentos individuales aparte de los *args o **kwargs
def multiplicacion(numero, *args):
    for i in args:
        resultado = numero*i
        print(f"El resultado es {resultado}")
multiplicacion(10,56,10)

print("\n")

# ------ *ARGS Y **KWARGS en una misma función ------
def datos(*args, **kwargs):
    print(args)
    print(kwargs)

usuario2 = {"nombre": "Maria", "apellido": "Julian", "edad": 35}

datos(10,"hola",True, **usuario2)

 


























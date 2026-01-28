# ------- Funciones Decoradoras --------
""" Es una función que envuelve otra función para añadir comportamiento
sin modificar la funcióm original, como un regalo, el decorador es el papel
y el moño, el regalo sigue siendo el mismo pero ahora 'hace/tiene' más cosas
"""

def a(b): #Función decoradora(encargada de decorar las funciones)
    def c(): #Función interna(envoltorio) que se retorna al mejorar la decorada
        #Código de función c
        b() #Función externa que será decorada
        #Más codigo.....
    return c

""" El flujo es el siguiente:

    1. Tienes una función decoradora
    2. Tienes muchas funciones que repiten código y quieres evitarlo
    3. Ingresas cada una de esas funciones como párametro en la
    función decoradora
    4. Te retorna las funciones funcionando correctamente y con
    el código que se repetía innecesariamente
    5. Eres feliz >:)
    
    """

# ------ EJEMPLO ------

""" Tienes tu función decoradora, recibes la función a decorar como parametro
y retornas una nueva función mejorada(decorada). Imagina una calculadora,
tienes funciones por cada operación, pero esas funciones repiten mensajes
como 'El resultado de la operación es' o 'Operación realizada con éxito!',
entonces decides meter esas funciones por el decorador, y así ahorras tiempo
y mejoras(decoras) la función original """

print("---------------- EJERCICIO 1 ------------------\n")
def decorador(func):
    def wrapper():
        print(f"El resultado de la operación es: ")
        func()
        print(f"Operación realizada con éxito!\n")
    return wrapper

def sumar():
    #Antes mensajes repetidos por funciones....
    print(10 + 10)

#Forma manual de guardar la nueva función en una variable(no recomendada porque
#'crea' o renombra la función)

# Acá la función sumar pasa a ser igual que el envoltorio
ab = decorador(sumar)
ab() #Función sumar decorada

#Decorador aplicado de forma automática a la función sin crear una nueva
#Forma correcta :)
@decorador
def restar():
    print(10 - 10)
restar()


# -------- EJEMPLO 2 ARGUMENTOS -------
""" Las funciones pueden ingresar un número indefinido de párametros
dependiendo el contexto y la necesidad de dicha función, por ello, el
envoltorio o la función decorada(wrapper) generalmente debe aceptar párametros
indefinidos, haciendo uso de *args y **kwargs. Si bien no es obligatorio
por buenas prácticas y correcto rendimiento de los decoradores se utilizan,
de lo contrario, no tendrian mucho sentido. """

print("---------------- EJERCICIO 2 ------------------\n")
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes del envoltorio")
        resultado = func(*args, **kwargs)
        print("Después del envoltorio")
        print("\n")
        return resultado
    return wrapper

@decorador
def usuario(nombre, edad, ciudad=None):
    return print(f"Me llamo {nombre} tengo {edad} años y vivo en {ciudad}.")

usuario("Andrés",21,ciudad="Bogotá")


print("---------------- EJERCICIO 3 ------------------\n")

# ------- EJEMPLO COMPLETO DE USO -------
""" En este ejemplo simulamos un login con sesión activa o inactiva, si
el usuario se logea la sesión se activa, si las credenciales son inválidas
no le permite acceder a rutas(funciones) de alguien logeado."""

USERS_DB = { "andres": "andy123",
          "maria": "mary4"
          }

session = {"user": None}

#Función para logearse(esta no será decorada)
def login(username, password):
    if username in USERS_DB and USERS_DB[username] == password:
        session["user"] = username
        print(f"!! {username.capitalize()} ha iniciado sesión éxitosamente")
    else:
        print("Usuario o contraseña incorrectos")

#Decorador
def login_required(func):
    def wrapper(*args, **kwargs):
        if session["user"] is None:
            print("Acceso denegado, debes iniciar sesión primero")
            return
        return func(*args, **kwargs)
    return wrapper

#Funciones que serán decoradas(el decorador verifica si esta logeado el usuario)
@login_required
def dashboard():
    print(f"Bienvenido a la Dashboard {session['user'].capitalize()}")
@login_required
def ver_presupuestos():
    print("Mostrando presupuestos....")

# -- Pruebas --

#Caso 1: Sin login
print("Sin login")
dashboard()
ver_presupuestos()
print("\n")

#Caso 2: Login incorrecto
print("Login incorrecto")
login("maria","0000")
dashboard()
print("\n")

#Caso 3: Login correcto
print("Login correcto")
login("maria","mary4")
dashboard()
ver_presupuestos()
print("\n")

#Caso 4: Logout
@login_required
def logout():
    print(f"{session['user'].capitalize()} ha cerrado sesión")
    session['user'] = None
    
print("Logout")
logout()
dashboard()
ver_presupuestos()
print("\n")














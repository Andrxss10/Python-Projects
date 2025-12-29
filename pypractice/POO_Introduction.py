# Programación Orientada a Objetos
"""Una clase es una especie de generador de objetos, como por ejemplo
tazas de diferentes colores, tamaños, limpieza, estilo, etc"""

"""Es algo asi cómo un respawn de minecraft"""

class Vehiculo():
    
    #Atributos
    ruedas = 4
    puertas = 4
    limpio = True
    color = None
    longitud_metros = None

    #Métodos    
    def prender(self):
        print("El vehiculo ha prendido")

    def acelerar(self):
        print("El vehiculo ha acelerado")

    def frenar(self):
        print("El vehiculo ha frenado")

print("--------- vehiculo 1 --------")
#Instanciamos el objeto(creamos un nuevo objeto)
vehiculo_1 = Vehiculo()

#Esta parte imprime la dirección de memoria del objeto instanciado
print(vehiculo_1)

#Imprimimos los atributos de la clase Vehiculo
print(vehiculo_1.ruedas)
print(vehiculo_1.puertas)
print(vehiculo_1.limpio)
print(vehiculo_1.color)
print(vehiculo_1.longitud_metros)
#Ejecutamos los métodos de la clase Vehiculo
vehiculo_1.prender()
vehiculo_1.acelerar()
vehiculo_1.frenar()

print("--------- vehiculo 2 --------")
#Si queremos crear un atributo único para un objeto lo hacemos asi:
vehiculo_2 = Vehiculo()

vehiculo_2.material_aleron = "Fibra de carbono"
print(vehiculo_2.material_aleron)













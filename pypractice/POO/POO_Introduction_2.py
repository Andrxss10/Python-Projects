#Declaramos la clase Vehiculo
class Vehiculo():

    pais_origen = "Alemania"
    
    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    def arrancar(self):
        print("El vehículo ha arrancado")

    def detener(self):
        print("El vehículo se ha detenido")

    def info_vehiculo(self):
        print(f"El vehiculo es de color {self.color}, tiene {self.ruedas} ruedas y ha andado {self.longitud_metros} km. ")
        print(f"Y proviene de {self.pais_origen}")
#Instanciamos el objeto y le pasamos los valores requeridos como párametros
vehiculo_1 = Vehiculo("Rojo", 2878.48, 4)
vehiculo_2 = Vehiculo("Amarillo", 0, 4)

print(vehiculo_1.pais_origen)

vehiculo_1.info_vehiculo()
vehiculo_2.info_vehiculo() 

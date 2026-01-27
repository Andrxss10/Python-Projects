class Motocicleta():
    estado = "nueva"
    motor = False
    
    def __init__(self, color, matricula, combustible_litros, tope_combustible, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.tope_combustible = tope_combustible
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
    def arrancar(self):
        if self.motor == True:
            print("El motor ya estaba arrancado.")
        else:
            self.motor = True
            print("Se ha arrancado el motor.")
    def detener(self):
        if self.motor == True:
            self.motor = False
            print("El motor se ha detenido.")
        else:
            print("El motor ya está detenido")

    def consulta_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es: {self.precio_mercado} COP $")

    def reporte_deposito(self):
        print(f"--- Reporte De Depósito de {self.marca.capitalize()} {self.modelo} ---")
        print(f"El depósito tiene {self.combustible_litros} litros.")
        print(f"La capacidad máxima del tanque es de {self.tope_combustible} litros")
        print(f"Faltan {self.tope_combustible - self.combustible_litros} litros para llenar el tanque")
        print("--- Fin del Reporte ---")

    def repostar(self):
        while True:
            self.repostar = float(input("Por favor, ingresa la cantidad de litros que deseas repostar: "))
            
            if (self.repostar + self.combustible_litros) <= self.tope_combustible:
                self.combustible_litros += self.repostar
                print(f"Has reposteado la moto con {self.repostar} litros. Deposito de combustible actual: {self.combustible_litros} litros")
                break
            else:
                print("La cantidad que quieres repostear supera el tope del deposito de la moto.")
                print(f"Combustible actual en la moto: {self.combustible_litros}")
                print(f"Tope del deposito de combustible de la moto: {self.tope_combustible}")
        
    
motocicleta_1 = Motocicleta("Rojo","ABC123",10,17,2,"Susuki","2026","14 de septiembre de 2025",260,2)

motocicleta_2 = Motocicleta(peso = 2, velocidad_punta = 295, fecha_fabricacion = "Enero 2014",
                            modelo = "2020", marca = "Yamaha", numero_ruedas = 2, combustible_litros = 0,
                            matricula = "DOUBLE-G 574", color = "Dorado", tope_combustible = 20)

#print(f"El motor de la moto 1 esta: {motocicleta_1.motor}")
#motocicleta_1.arrancar()
#print(f"El motor de la moto 1 cambio a: {motocicleta_1.motor}")


#print(f"El motor de la moto 2 esta: {motocicleta_2.motor}")
#motocicleta_2.detener()
#print(f"El motor de la moto 2 ya esta detenido: {motocicleta_2.motor}")


#Añadir precio a la segunda motocicleta desde fuera:
motocicleta_2.precio_mercado = 27000000

#motocicleta_2.consulta_precio()
#motocicleta_1.reporte_deposito()

motocicleta_2.repostar()
motocicleta_2.reporte_deposito()



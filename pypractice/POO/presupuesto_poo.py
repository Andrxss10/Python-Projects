from abc import ABC, abstractmethod

#Abstración
class Movimiento(ABC):
    """
    Clase abstracta que representa un movimiento financiero.
    Puede ser un Gasto o un Ingreso, pero las clases que la heredan
    si o si deben implementar esta función, por obligación de la
    abstración.
    """

    def __init__(self, descripcion, monto):
        self.descripcion = descripcion
        self.monto = monto

    @abstractmethod
    def tipo(self):
        """
        Debe devolver el tipo de movimiento"""
        pass

#Herencia
#Un Gasto ES: un movimiento (representación de herencia)
class Gasto(Movimiento):
    """
    Represemta un gasto del movimiento
    """
    def tipo(self):
        return "Gasto"

    
#Un Ingreso ES: un movimiento (representación de herencia)
class Ingreso(Movimiento):
    """
    Represemta un gasto del movimiento
    """
    def tipo(self):
        return "Ingreso"

class Presupuesto():

    """ Maneja ingresos y gastos """
    moneda = "COP" #Atributo de clase, solo por el ejemplo porque no es necesario

    def __init__(self, nombre):
        self.nombre = nombre
        self.__movimientos = [] # Atributo privado - (se utiliza __ antes)

    def agregar_movimiento(self, movimiento):

        #Si el argumento movimiento no es instancia de la clase Movimiento:
        if not isinstance(movimiento, Movimiento):
            raise TypeError("Debe ser un movimiento válido")
        self.__movimientos.append(movimiento)
    
    def total_ingresos(self):   
        return sum(m.monto for m in self.__movimientos if m.tipo() == "Ingreso")#Polimorfismo

    def total_gastos(self):
        return sum(m.monto for m in self.__movimientos if m.tipo() == "Gasto")#Polimorfismo

    def balance(self):
        return self.total_ingresos() - self.total_gastos()

    def resumen(self):
        print(f"\n Presupuesto: {self.nombre}")
        for m in self.__movimientos:
            # Iteracion movimiento por movimiento
            print(f"\n- {m.tipo()}: {m.descripcion} --> {m.monto} {self.moneda}\n")
            
        # Total de Ingresos
        print(f"Ingresos Totales: {self.total_ingresos()} {self.moneda}\n")

        # Total de Gastos
        print(f"Gastos Totales: {self.total_gastos()} {self.moneda}\n")
        
        # Balance
        print(f"Balance: {self.balance()} {self.moneda}\n")


if __name__ == "__main__":
    # Creamos una nueva instancia(objeto) de la clase presupuesto
    presupuesto = Presupuesto("Nuevo presupuesto Enero 2026")

""" Polimorfismo: misma función diferente comportamiento """

#Polimorfismo(agregar_movimiento gasto o ingreso = usar cosas distintas como iguales)
# Agregamos movimientos al presupuesto (gasto o ingreso)

#Gasto
presupuesto.agregar_movimiento(Gasto("Mercado del mes",125))

#Ingreso
presupuesto.agregar_movimiento(Ingreso("Salario mensual",500))

#Gasto
presupuesto.agregar_movimiento(Gasto("Arriendo",250))

#Ingreso
presupuesto.agregar_movimiento(Ingreso("Domingo de trabajo extra",20))

#Gasto
presupuesto.agregar_movimiento(Gasto("Pasajes del mes",50))

presupuesto.resumen()













































































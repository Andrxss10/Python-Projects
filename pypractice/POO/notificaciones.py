from abc import ABC, abstractmethod

class Notificacion(ABC):

    proveedor = "Sistema central"

    def __init__(self, mensaje):
        self._mensaje = mensaje

    @abstractmethod
    def enviar(self):
        pass

class Email(Notificacion):

    def enviar(self):
        print(f"[EMAIL] {self._mensaje}")

class SMS(Notificacion):

    def enviar(self):
        print(f"[SMS] {self._mensaje}")

class Push(Notificacion):

    def enviar(self):
        print(f"[PUSH] {self._mensaje}")


class SistemaNotificaciones:
    def __init__(self):
        self._notificaciones = []

    def agregar(self, notificacion):
        self._notificaciones.append(notificacion)

    def enviar(self):
        for n in self._notificaciones:
            n.enviar() # Polimorfismo real, toma las notificaciones como igual

if __name__ == "__main__":
    
    sistema = SistemaNotificaciones()

sistema.agregar(Email("Hola por email"))
sistema.agregar(SMS("Hola por SMS"))
sistema.agregar(Push("Hola por push"))

sistema.enviar()





    

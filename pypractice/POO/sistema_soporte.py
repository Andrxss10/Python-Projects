from abc import ABC, abstractmethod

class Ticket(ABC):

    _contador_id = 0
    
    def __init__(self, descripcion):
        Ticket._contador_id += 1
        self._id = Ticket._contador_id
        self.descripcion = descripcion
        self.__estado = "abierto"

    @abstractmethod
    def procesar(self):
        pass

    def cerrar_ticket(self):
        self.__estado = "cerrado"

class TicketSoporteTecnico(Ticket):

    def procesar(self):
        print(f"Procesando la solicitud:\n"
              f"Ticket id: {self._id} \n"
              f"Descripcion: {self.descripcion}\n"
              f"Tipo de ticket: Soporte Técnico\n")

class TicketFacturacion(Ticket):

    def procesar(self):
        print(f"Procesando la solicitud:\n"
              f"Ticket id: {self._id} \n"
              f"Descripcion: {self.descripcion}\n"
              f"Tipo de ticket: Facturación\n")

class TicketSugerencia(Ticket):

    def procesar(self):
        print(f"Procesando la solicitud:\n"
              f"Ticket id: {self._id} \n"
              f"Descripcion: {self.descripcion}\n"
              f"Tipo de ticket: Sugerencia\n")

class SistemaSoporte:

    def __init__(self):
        self.tickets = []

    def agregar_ticket(self, ticket):
        self.tickets.append(ticket)

    def procesar_todos(self):
        for ticket in self.tickets:
            ticket.procesar()


if __name__ == "__main__":
    soporte = SistemaSoporte()

    t1 = TicketSoporteTecnico("No prende el computador")
    t2 = TicketFacturacion("Cobro incorrecto")
    t3 = TicketSugerencia("Podrían permitir más medios de pago")
    
    soporte.agregar_ticket(t1)
    soporte.agregar_ticket(t2)
    soporte.agregar_ticket(t3)

    soporte.procesar_todos()
            





























        

import logging
from excepciones import ErrorReserva


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.servicio is None:
            raise ErrorReserva("No se puede confirmar sin servicio")

        self.estado = "Confirmada"
        logging.info(f"Reserva {self.estado} para cliente {self.cliente.nombre}")
        return "Reserva confirmada"

    def cancelar(self):
        self.estado = "Cancelada"
        logging.info(f"Reserva {self.estado} para cliente {self.cliente.nombre}")
        return "Reserva cancelada"

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo() * self.duracion
            return f"Costo total: {costo}"
        except Exception as e:
            raise ErrorReserva(f"Error al procesar reserva: {e}")
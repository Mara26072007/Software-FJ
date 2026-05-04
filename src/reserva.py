import logging
from excepciones import ErrorReserva

# Configuración del logger para registrar eventos de reservas
logging.basicConfig(filename="sistema.log", level=logging.INFO)


class Reserva:
    """
    Clase que representa una reserva de servicio para un cliente en Software FJ.
    Integra cliente, servicio, duración y estado.
    Implementa confirmación, cancelación y procesamiento con manejo
    robusto de excepciones: try/except, try/except/else y try/except/finally.
    """

    # Estados posibles de una reserva
    ESTADO_PENDIENTE  = "Pendiente"
    ESTADO_CONFIRMADA = "Confirmada"
    ESTADO_CANCELADA  = "Cancelada"

    def __init__(self, cliente, servicio, duracion: int):
        """
        Inicializa la reserva validando todos los parámetros recibidos.
        Lanza ErrorReserva si algún parámetro es inválido.
        """
        try:
            # Validación del cliente
            if cliente is None:
                raise ErrorReserva("El cliente no puede ser nulo.")

            # Validación del servicio
            if servicio is None:
                raise ErrorReserva("El servicio no puede ser nulo.")

            # Validación de la duración: debe ser entero positivo
            if not isinstance(duracion, int) or duracion <= 0:
                raise ErrorReserva(
                    f"La duración debe ser un entero positivo. Se recibió: {duracion}"
                )

            self.cliente  = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado   = self.ESTADO_PENDIENTE

            logging.info(
                f"Reserva creada para cliente '{self.cliente.nombre}' | "
                f"Servicio: '{self.servicio.nombre}' | Duración: {self.duracion}h"
            )

        except ErrorReserva as e:
            # Encadenamiento de excepción: registra y relanza con contexto
            logging.error(f"Error al crear reserva: {e}")
            raise ErrorReserva(f"No se pudo crear la reserva: {e}") from e

    # ─────────────────────────────────────────
    #  CONFIRMAR RESERVA — usa try/except/else
    # ─────────────────────────────────────────
    def confirmar(self) -> str:
        """
        Confirma la reserva si está en estado Pendiente.
        Usa try/except/else: el bloque else solo se ejecuta si no hubo excepción.
        """
        try:
            # Verificamos que la reserva no esté ya procesada
            if self.estado != self.ESTADO_PENDIENTE:
                raise ErrorReserva(
                    f"No se puede confirmar una reserva en estado '{self.estado}'."
                )
        except ErrorReserva as e:
            logging.error(f"Error al confirmar reserva de '{self.cliente.nombre}': {e}")
            raise
        else:
            # Este bloque SOLO se ejecuta si NO hubo excepción en el try
            self.estado = self.ESTADO_CONFIRMADA
            logging.info(f"Reserva confirmada para '{self.cliente.nombre}'.")
            return f"✅ Reserva confirmada para {self.cliente.nombre} | Servicio: {self.servicio.nombre}"

    # ─────────────────────────────────────────
    #  CANCELAR RESERVA — usa try/except/finally
    # ─────────────────────────────────────────
    def cancelar(self) -> str:
        """
        Cancela la reserva si no está ya cancelada.
        Usa try/except/finally: el bloque finally siempre se ejecuta
        para registrar el intento en el log.
        """
        try:
            if self.estado == self.ESTADO_CANCELADA:
                raise ErrorReserva("La reserva ya está cancelada.")

            self.estado = self.ESTADO_CANCELADA

        except ErrorReserva as e:
            logging.error(f"Error al cancelar reserva de '{self.cliente.nombre}': {e}")
            raise
        finally:
            # Este bloque se ejecuta SIEMPRE, haya o no excepción
            logging.info(
                f"Intento de cancelación registrado para '{self.cliente.nombre}' | "
                f"Estado final: {self.estado}"
            )

        return f"❌ Reserva cancelada para {self.cliente.nombre} | Servicio: {self.servicio.nombre}"

    # ─────────────────────────────────────────
    #  PROCESAR RESERVA — usa try/except/else/finally
    # ─────────────────────────────────────────
    def procesar(self) -> str:
        """
        Procesa el cálculo del costo total de la reserva.
        Usa try/except/else/finally para manejar todos los casos posibles.
        """
        costo_total = None
        try:
            # Solo se puede procesar si está confirmada
            if self.estado != self.ESTADO_CONFIRMADA:
                raise ErrorReserva(
                    f"Solo se pueden procesar reservas confirmadas. "
                    f"Estado actual: '{self.estado}'."
                )
            # Calcula el costo usando el servicio y la duración
            costo_total = self.servicio.calcular_costo(duracion=self.duracion)

        except ErrorReserva as e:
            logging.error(f"ErrorReserva al procesar para '{self.cliente.nombre}': {e}")
            raise
        except Exception as e:
            # Captura cualquier otro error inesperado y lo encadena
            logging.error(f"Error inesperado al procesar reserva: {e}")
            raise ErrorReserva(f"Error inesperado al procesar la reserva: {e}") from e
        else:
            # Solo se ejecuta si el cálculo fue exitoso
            logging.info(
                f"Reserva procesada para '{self.cliente.nombre}': "
                f"costo total=${costo_total:.2f}"
            )
            return (
                f"💰 Costo total para {self.cliente.nombre} | "
                f"Servicio: {self.servicio.nombre} | "
                f"Duración: {self.duracion}h | "
                f"Total: ${costo_total:.2f}"
            )
        finally:
            # Siempre se registra el intento de procesamiento
            logging.info(
                f"Procesamiento finalizado para '{self.cliente.nombre}' | "
                f"Estado: {self.estado}"
            )

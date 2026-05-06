from abc import ABC, abstractmethod
import logging
from excepciones import ErrorServicio

# Configuración del logger para registrar eventos de servicios
logging.basicConfig(filename="sistema.log", level=logging.INFO)


# ─────────────────────────────────────────────
#  CLASE ABSTRACTA BASE
# ─────────────────────────────────────────────
class Servicio(ABC):
    """
    Clase abstracta que representa un servicio genérico de Software FJ.
    Todas las clases de servicio concretas deben heredar de esta clase
    e implementar los métodos abstractos definidos aquí.
    """

    def __init__(self, nombre: str, costo_base: float):
        """
        Inicializa el servicio con nombre y costo base.
        Valida que el costo base sea un valor positivo.
        """
        # Validación del nombre del servicio
        if not nombre or not nombre.strip():
            raise ErrorServicio("El nombre del servicio no puede estar vacío.")

        # Validación del costo base: no puede ser negativo ni cero
        if not isinstance(costo_base, (int, float)) or costo_base <= 0:
            raise ErrorServicio(
                f"El costo base debe ser un número positivo. Se recibió: {costo_base}"
            )

        self._nombre = nombre.strip()
        self._costo_base = costo_base
        logging.info(f"Servicio '{self._nombre}' creado con costo base ${self._costo_base}.")

    # ── Getters ──────────────────────────────
    @property
    def nombre(self):
        """Retorna el nombre del servicio."""
        return self._nombre

    @property
    def costo_base(self):
        """Retorna el costo base del servicio."""
        return self._costo_base

    # ── Métodos abstractos ───────────────────
    @abstractmethod
    def calcular_costo(self, duracion: int = 1, descuento: float = 0.0) -> float:
        """
        Calcula el costo total del servicio según duración y descuento.
        Debe ser implementado por cada subclase.
        """
        pass

    @abstractmethod
    def describir(self) -> str:
        """
        Retorna una descripción detallada del servicio.
        Debe ser implementado por cada subclase (polimorfismo).
        """
        pass

    def validar_parametros(self, duracion: int, descuento: float):
        """
        Valida que los parámetros de cálculo sean correctos.
        Método compartido por todas las subclases.
        Lanza ErrorServicio si algún parámetro es inválido.
        """
        if not isinstance(duracion, int) or duracion <= 0:
            raise ErrorServicio(
                f"La duración debe ser un número entero positivo. Se recibió: {duracion}"
            )
        if not isinstance(descuento, (int, float)) or not (0.0 <= descuento < 1.0):
            raise ErrorServicio(
                f"El descuento debe ser un valor entre 0.0 y 0.99. Se recibió: {descuento}"
            )


# ─────────────────────────────────────────────
#  SERVICIO 1: RESERVA DE SALA
# ─────────────────────────────────────────────
class ServicioSala(Servicio):
    """
    Servicio de reserva de salas de reuniones.
    Aplica un impuesto del 10% sobre el costo base por hora.
    """

    IMPUESTO = 0.10

    def calcular_costo(self, duracion: int = 1, descuento: float = 0.0) -> float:
        """
        Calcula el costo de reserva de sala.
        Fórmula: (costo_base * (1 + impuesto) * duracion) * (1 - descuento)
        Parámetros opcionales permiten sobrecarga de comportamiento.
        """
        self.validar_parametros(duracion, descuento)
        costo = self._costo_base * (1 + self.IMPUESTO) * duracion
        costo_final = costo * (1 - descuento)
        logging.info(
            f"ServicioSala '{self._nombre}': duración={duracion}h, "
            f"descuento={descuento*100}%, costo final=${costo_final:.2f}"
        )
        return round(costo_final, 2)

    def describir(self) -> str:
        """Descripción del servicio de sala."""
        return (
            f"[Reserva de Sala] '{self._nombre}' | "
            f"Costo base: ${self._costo_base}/h | "
            f"Impuesto: {self.IMPUESTO*100}%"
        )


# ─────────────────────────────────────────────
#  SERVICIO 2: ALQUILER DE EQUIPO
# ─────────────────────────────────────────────
class ServicioEquipo(Servicio):
    """
    Servicio de alquiler de equipos tecnológicos.
    Aplica un cargo de mantenimiento del 20% sobre el costo base.
    """

    CARGO_MANTENIMIENTO = 0.20

    def calcular_costo(self, duracion: int = 1, descuento: float = 0.0) -> float:
        """
        Calcula el costo de alquiler de equipo.
        Fórmula: (costo_base * (1 + mantenimiento) * duracion) * (1 - descuento)
        """
        self.validar_parametros(duracion, descuento)
        costo = self._costo_base * (1 + self.CARGO_MANTENIMIENTO) * duracion
        costo_final = costo * (1 - descuento)
        logging.info(
            f"ServicioEquipo '{self._nombre}': duración={duracion}h, "
            f"descuento={descuento*100}%, costo final=${costo_final:.2f}"
        )
        return round(costo_final, 2)

    def describir(self) -> str:
        """Descripción del servicio de equipo."""
        return (
            f"[Alquiler de Equipo] '{self._nombre}' | "
            f"Costo base: ${self._costo_base}/h | "
            f"Cargo mantenimiento: {self.CARGO_MANTENIMIENTO*100}%"
        )


# ─────────────────────────────────────────────
#  SERVICIO 3: ASESORÍA ESPECIALIZADA
# ─────────────────────────────────────────────
class ServicioAsesoria(Servicio):
    """
    Servicio de asesoría especializada por consultores.
    Aplica un cargo de consultoría del 30% sobre el costo base.
    """

    CARGO_CONSULTORIA = 0.30

    def calcular_costo(self, duracion: int = 1, descuento: float = 0.0) -> float:
        """
        Calcula el costo de asesoría especializada.
        Fórmula: (costo_base * (1 + consultoría) * duracion) * (1 - descuento)
        """
        self.validar_parametros(duracion, descuento)
        costo = self._costo_base * (1 + self.CARGO_CONSULTORIA) * duracion
        costo_final = costo * (1 - descuento)
        logging.info(
            f"ServicioAsesoria '{self._nombre}': duración={duracion}h, "
            f"descuento={descuento*100}%, costo final=${costo_final:.2f}"
        )
        return round(costo_final, 2)

    def describir(self) -> str:
        """Descripción del servicio de asesoría."""
        return (
            f"[Asesoría Especializada] '{self._nombre}' | "
            f"Costo base: ${self._costo_base}/h | "
            f"Cargo consultoría: {self.CARGO_CONSULTORIA*100}%"
        )

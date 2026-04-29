from abc import ABC, abstractmethod


class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass


class ServicioSala(Servicio):
    def calcular_costo(self):
        return self.costo_base * 1.10  # incluye impuesto


class ServicioEquipo(Servicio):
    def calcular_costo(self):
        return self.costo_base * 1.20  # incluye mantenimiento


class ServicioAsesoria(Servicio):
    def calcular_costo(self):
        return self.costo_base * 1.30  # incluye consultoría
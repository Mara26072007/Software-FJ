from abc import ABC, abstractmethod


class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, duracion=1, descuento=0):
        pass

servicio1 = Servicio("Servicio 1", 100)
costo_total = servicio1.calcular_costo(duracion=2, descuento=0.1)
print(f"Costo total: {costo_total}")


class ServicioSala(Servicio):
    def calcular_costo(self, duracion=1, descuento=0):
        costo = self.costo_base * 1.10  # incluye impuesto
        return costo - (costo * descuento)


class ServicioEquipo(Servicio):
    def calcular_costo(self, duracion=1, descuento=0):
        costo = self.costo_base * 1.20  # incluye mantenimiento
        return costo - (costo * descuento)


class ServicioAsesoria(Servicio):
    def calcular_costo(self, duracion=1, descuento=0):
        costo = self.costo_base * 1.30  # incluye consultoría
        return costo - (costo * descuento)
class Cliente:
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono

    def mostrar_info(self):
        return f"Cliente: {self.nombre} - Documento: {self.documento}"
from excepciones import ErrorCliente


class Cliente:
    def __init__(self, nombre, documento, telefono):
        self.__nombre = nombre
        self.__documento = documento
        self.__telefono = telefono

        self.__validar_datos()

    #  Encapsulación (Getters)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def telefono(self):
        return self.__telefono

    #  Encapsulación (Setters con validación)
    @nombre.setter
    def nombre(self, value):
        if not value or not value.strip():
            raise ErrorCliente("El nombre no puede estar vacío")
        self.__nombre = value

    @documento.setter
    def documento(self, value):
        if not value.isdigit():
            raise ErrorCliente("El documento debe ser numérico")
        self.__documento = value

    @telefono.setter
    def telefono(self, value):
        if not value.isdigit() or len(value) < 7:
            raise ErrorCliente("Teléfono inválido")
        self.__telefono = value

    #  Validación interna
    def __validar_datos(self):
        try:
            if not self.__nombre or not self.__nombre.strip():
                raise ErrorCliente("El nombre no puede estar vacío")

            if not self.__documento.isdigit():
                raise ErrorCliente("El documento debe ser numérico")

            if not self.__telefono.isdigit() or len(self.__telefono) < 7:
                raise ErrorCliente("Teléfono inválido")

        except ErrorCliente as e:
            # Encadenamiento de excepción
            raise ErrorCliente(f"Error al crear cliente: {e}") from e

    #  Método funcional
    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - Documento: {self.__documento} - Teléfono: {self.__telefono}"
from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva
from excepciones import ErrorCliente, ErrorReserva, ErrorServicio
import logging
logging.basicConfig(filename="sistema.log", level=logging.INFO)

print("=== SISTEMA SOFTWARE FJ ===")

# 1. Crear cliente válido
cliente1 = Cliente("Juan Pérez", "12345", "3001234567")
print("Cliente válido creado")

# 2. Crear servicios
servicio1 = ServicioSala("Sala reuniones", 100)
servicio2 = ServicioEquipo("Computador", 200)
servicio3 = ServicioAsesoria("Asesoría TI", 300)

# 3. Crear reservas
reserva1 = Reserva(cliente1, servicio1, 2)
reserva2 = Reserva(cliente1, servicio2, 1)

# 4. Operaciones correctas
print(reserva1.confirmar())
print(reserva1.procesar())

print(reserva2.confirmar())
print(reserva2.procesar())

# 5. Caso de error controlado
try:
    reserva_error = Reserva(cliente1, None, 1)
    reserva_error.confirmar()
except ErrorReserva as e:
    print("Error controlado:", e)

# 6. Cancelación
print(reserva2.cancelar())

print("=== FIN DEL SISTEMA ===")

# 7. Cliente inválido (nombre vacío, documento no numérico)
try:
    cliente_invalido = Cliente("", "abc", "123")
except ErrorCliente as e:
    print("Error controlado:", e)

# 8. Servicio con costo negativo
try:
    servicio_invalido = ServicioSala("Sala pequeña", -50)
    print(servicio_invalido.calcular_costo())
except ErrorServicio as e:
    print("Error controlado:", e)

# 9. Reserva con duración inválida
try:
    reserva_invalida = Reserva(cliente1, servicio1, -2)
    print(reserva_invalida.procesar())
except ErrorReserva as e:
    print("Error controlado:", e)

# 10. Reserva cancelada correctamente
print(reserva1.cancelar())

from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva
from excepciones import ErrorReserva

print("=== SISTEMA SOFTWARE FJ ===")

# 1. Crear cliente válido
cliente1 = Cliente("Juan Pérez", "12345", "3001234567")
print("Prueba realizada por Emilson - trabajo colaborativo")

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
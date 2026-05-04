"""
Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación 213023 - UNAD
Descripción: Punto de entrada principal. Simula 10 operaciones completas
             demostrando el manejo robusto de excepciones.
"""

import logging
from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva

# ── Configuración del sistema de logs ────────────────────────────────────────
logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ── Función auxiliar para separar visualmente cada operación ─────────────────
def titulo(numero: int, descripcion: str):
    print(f"\n{'='*60}")
    print(f"  OPERACIÓN {numero}: {descripcion}")
    print(f"{'='*60}")


print("\n🏢  SISTEMA INTEGRAL SOFTWARE FJ  🏢")
print("Iniciando simulación de operaciones...\n")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 1 — Registro de cliente válido
# ════════════════════════════════════════════════════════════
titulo(1, "Registro de cliente válido")
try:
    cliente1 = Cliente("Ana Torres", "10234567", "3001234567")
    print(cliente1.mostrar_info())
except ErrorCliente as e:
    print(f"Error: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 2 — Registro de cliente con datos inválidos
# ════════════════════════════════════════════════════════════
titulo(2, "Registro de cliente con datos inválidos (nombre vacío, doc no numérico)")
try:
    cliente_invalido = Cliente("", "ABC", "123")
    print(cliente_invalido.mostrar_info())
except ErrorCliente as e:
    print(f"⚠️  Error controlado: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 3 — Creación correcta de tres servicios
# ════════════════════════════════════════════════════════════
titulo(3, "Creación correcta de servicios")
try:
    sala      = ServicioSala("Sala de Reuniones A", 100)
    equipo    = ServicioEquipo("Portátil HP ProBook", 200)
    asesoria  = ServicioAsesoria("Asesoría en Ciberseguridad", 300)

    # Polimorfismo: llamamos describir() en cada objeto de distinto tipo
    for servicio in [sala, equipo, asesoria]:
        print(servicio.describir())
except ErrorServicio as e:
    print(f"Error: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 4 — Creación de servicio con costo negativo
# ════════════════════════════════════════════════════════════
titulo(4, "Creación de servicio con costo inválido (negativo)")
try:
    servicio_malo = ServicioSala("Sala rota", -50)
except ErrorServicio as e:
    print(f"⚠️  Error controlado: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 5 — Reserva exitosa: confirmar y procesar
# ════════════════════════════════════════════════════════════
titulo(5, "Reserva exitosa: crear, confirmar y procesar")
try:
    reserva1 = Reserva(cliente1, sala, 3)
    print(reserva1.confirmar())
    print(reserva1.procesar())
except (ErrorReserva, ErrorServicio) as e:
    print(f"Error: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 6 — Reserva con descuento (sobrecarga de parámetros)
# ════════════════════════════════════════════════════════════
titulo(6, "Reserva con descuento del 15% (sobrecarga calcular_costo)")
try:
    cliente2  = Cliente("Carlos Mendez", "98765432", "3109876543")
    reserva2  = Reserva(cliente2, asesoria, 2)
    print(reserva2.confirmar())
    # Llamada con parámetros opcionales: sobrecarga de comportamiento
    costo = asesoria.calcular_costo(duracion=2, descuento=0.15)
    print(f"💰 Costo con descuento 15%: ${costo:.2f}")
except (ErrorCliente, ErrorReserva, ErrorServicio) as e:
    print(f"Error: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 7 — Intento de procesar reserva sin confirmar
# ════════════════════════════════════════════════════════════
titulo(7, "Procesar reserva que NO está confirmada")
try:
    reserva3 = Reserva(cliente1, equipo, 1)
    # Intentamos procesar sin confirmar primero → debe lanzar excepción
    print(reserva3.procesar())
except ErrorReserva as e:
    print(f"⚠️  Error controlado: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 8 — Reserva con duración inválida
# ════════════════════════════════════════════════════════════
titulo(8, "Reserva con duración inválida (número negativo)")
try:
    reserva_invalida = Reserva(cliente1, sala, -3)
except ErrorReserva as e:
    print(f"⚠️  Error controlado: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 9 — Cancelación de reserva y reintento
# ════════════════════════════════════════════════════════════
titulo(9, "Cancelar reserva y luego intentar cancelar de nuevo")
try:
    reserva4 = Reserva(cliente2, equipo, 4)
    reserva4.confirmar()
    print(reserva4.cancelar())
    # Intentar cancelar una reserva ya cancelada → debe lanzar excepción
    print(reserva4.cancelar())
except ErrorReserva as e:
    print(f"⚠️  Error controlado: {e}")

# ════════════════════════════════════════════════════════════
#  OPERACIÓN 10 — Encadenamiento de excepciones
# ════════════════════════════════════════════════════════════
titulo(10, "Encadenamiento de excepciones (cliente sin servicio asignado)")
try:
    reserva5 = Reserva(cliente1, None, 2)
except ErrorReserva as e:
    print(f"⚠️  Error controlado: {e}")
    if e.__cause__:
        print(f"   Causa original: {e.__cause__}")

# ── Fin del sistema ──────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("✅  Simulación finalizada. Revisa sistema.log para el registro completo.")
print(f"{'='*60}\n")
logging.info("Simulación completada exitosamente.")

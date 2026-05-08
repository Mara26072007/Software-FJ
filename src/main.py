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

logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Función auxiliar para mostrar títulos
def titulo(texto: str):
    print(f"\n{'='*60}\n{texto}\n{'='*60}")

# Menú principal
def menu():
    print("\n🏢 SISTEMA INTEGRAL SOFTWARE FJ 🏢")
    print("Seleccione una opción:")
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Confirmar reserva")
    print("5. Procesar reserva")
    print("6. Cancelar reserva")
    print("7. Salir")

# Variables globales para simular datos
clientes = []
servicios = []
reservas = []

# Funciones de operaciones
def registrar_cliente():
    titulo("Registro de cliente")
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    telefono = input("Teléfono: ")
    try:
        cliente = Cliente(nombre, documento, telefono)
        clientes.append(cliente)
        print("✅ Cliente registrado correctamente")
    except ErrorCliente as e:
        print(f"⚠️ Error: {e}")

def crear_servicio():
    titulo("Creación de servicio")
    print("1. Sala de reuniones\n2. Computador\n3. Asesoría TI")
    opcion = input("Seleccione tipo de servicio: ")
    nombre = input("Nombre del servicio: ")
    costo = float(input("Costo base: "))
    try:
        if opcion == "1":
            servicio = ServicioSala(nombre, costo)
        elif opcion == "2":
            servicio = ServicioEquipo(nombre, costo)
        elif opcion == "3":
            servicio = ServicioAsesoria(nombre, costo)
        else:
            print("⚠️ Opción inválida")
            return
        servicios.append(servicio)
        print("✅ Servicio creado correctamente")
    except ErrorServicio as e:
        print(f"⚠️ Error: {e}")

def crear_reserva():
    titulo("Creación de reserva")
    if not clientes or not servicios:
        print("⚠️ Debe registrar al menos un cliente y un servicio primero")
        return
    cliente = clientes[0]  # por simplicidad, tomamos el primero
    servicio = servicios[0]
    duracion = int(input("Duración (horas): "))
    try:
        reserva = Reserva(cliente, servicio, duracion)
        reservas.append(reserva)
        print("✅ Reserva creada correctamente")
    except ErrorReserva as e:
        print(f"⚠️ Error: {e}")

def confirmar_reserva():
    titulo("Confirmar reserva")
    if not reservas:
        print("⚠️ No hay reservas registradas")
        return
    print(reservas[0].confirmar())

def procesar_reserva():
    titulo("Procesar reserva")
    if not reservas:
        print("⚠️ No hay reservas registradas")
        return
    try:
        print(reservas[0].procesar())
    except ErrorReserva as e:
        print(f"⚠️ Error: {e}")

def cancelar_reserva():
    titulo("Cancelar reserva")
    if not reservas:
        print("⚠️ No hay reservas registradas")
        return
    try:
        print(reservas[0].cancelar())
    except ErrorReserva as e:
        print(f"⚠️ Error: {e}")

# Programa principal
if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Ingrese opción: ")
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            crear_servicio()
        elif opcion == "3":
            crear_reserva()
        elif opcion == "4":
            confirmar_reserva()
        elif opcion == "5":
            procesar_reserva()
        elif opcion == "6":
            cancelar_reserva()
        elif opcion == "7":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida")

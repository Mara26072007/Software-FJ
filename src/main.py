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

#  Función auxiliar para separar visualmente cada operación 
def titulo(numero: int, descripcion: str):
    print(f"\n{'='*60}")
    print(f"  OPERACIÓN {numero}: {descripcion}")
    print(f"{'='*60}")

# ════════════════════════════════════════════════════════════
# SIMULACIÓN AUTOMÁTICA (10 operaciones)
# ════════════════════════════════════════════════════════════
def simulacion_automatica():
    print("\n SISTEMA INTEGRAL SOFTWARE FJ - SIMULACIÓN AUTOMÁTICA")
    print("Iniciando simulación automática...\n")

    # Servicios base
    sala      = ServicioSala("Sala de Reuniones A", 100)
    equipo    = ServicioEquipo("Portátil HP ProBook", 200)
    asesoria  = ServicioAsesoria("Asesoría en Ciberseguridad", 300)

    # Operación 1
    titulo(1, "Registro de cliente válido")
    try:
        cliente1 = Cliente("Ana Torres", "10234567", "3001234567")
        print(cliente1.mostrar_info())
    except ErrorCliente as e:
        print(f"Error: {e}")

    # Operación 2
    titulo(2, "Registro de cliente inválido")
    try:
        Cliente("", "ABC", "123")
    except ErrorCliente as e:
        print(f" Error controlado: {e}")

    # Operación 3
    titulo(3, "Creación de servicios")
    for servicio in [sala, equipo, asesoria]:
        print(servicio.describir())

    # Operación 4
    titulo(4, "Servicio con costo negativo")
    try:
        ServicioSala("Sala rota", -50)
    except ErrorServicio as e:
        print(f" Error controlado: {e}")

    # Operación 5
    titulo(5, "Reserva exitosa")
    reserva1 = Reserva(cliente1, sala, 3)
    print(reserva1.confirmar())
    print(reserva1.procesar())

    # Operación 6
    titulo(6, "Reserva con descuento")
    cliente2 = Cliente("Carlos Mendez", "98765432", "3109876543")
    reserva2 = Reserva(cliente2, asesoria, 2)
    print(reserva2.confirmar())
    costo = asesoria.calcular_costo(duracion=2, descuento=0.15)
    print(f" Costo con descuento: ${costo:.2f}")

    # Operación 7
    titulo(7, "Procesar sin confirmar")
    try:
        reserva3 = Reserva(cliente1, equipo, 1)
        print(reserva3.procesar())
    except ErrorReserva as e:
        print(f" Error controlado: {e}")

    # Operación 8
    titulo(8, "Reserva con duración inválida")
    try:
        Reserva(cliente1, sala, -3)
    except ErrorReserva as e:
        print(f" Error controlado: {e}")

    # Operación 9
    titulo(9, "Cancelar reserva dos veces")
    reserva4 = Reserva(cliente2, equipo, 4)
    reserva4.confirmar()
    print(reserva4.cancelar())
    try:
        print(reserva4.cancelar())
    except ErrorReserva as e:
        print(f" Error controlado: {e}")

    # Operación 10
    titulo(10, "Reserva sin servicio")
    try:
        Reserva(cliente1, None, 2)
    except ErrorReserva as e:
        print(f" Error controlado: {e}")

    print("\n Simulación automática finalizada.")


# ════════════════════════════════════════════════════════════
# MODO INTERACTIVO (menú estilo aplicación)
# ════════════════════════════════════════════════════════════
clientes = []
servicios = []
reservas = []

def menu():
    print("\n SISTEMA INTEGRAL SOFTWARE FJ ")
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Confirmar reserva")
    print("5. Procesar reserva")
    print("6. Cancelar reserva")
    print("7. Salir")

def registrar_cliente():
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    telefono = input("Teléfono: ")
    try:
        cliente = Cliente(nombre, documento, telefono)
        clientes.append(cliente)
        print(" Cliente registrado")
    except ErrorCliente as e:
        print(f" Error: {e}")

def crear_servicio():
    print("1. Sala\n2. Computador\n3. Asesoría TI")
    opcion = input("Seleccione tipo: ")
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
            print(" Opción inválida")
            return
        servicios.append(servicio)
        print(" Servicio creado")
    except ErrorServicio as e:
        print(f" Error: {e}")

def crear_reserva():
    if not clientes or not servicios:
        print(" Opción inválida")
        return
    cliente = clientes[0]
    servicio = servicios[0]
    duracion = int(input("Duración (horas): "))
    try:
        reserva = Reserva(cliente, servicio, duracion)
        reservas.append(reserva)
        print(" Reserva creada")
    except ErrorReserva as e:
        print(f" Error: {e}")

def confirmar_reserva():
    if reservas:
        print(reservas[0].confirmar())
    else:
        print(" No hay reservas")

def procesar_reserva():
    if reservas:
        try:
            print(reservas[0].procesar())
        except ErrorReserva as e:
            print(f" Error: {e}")
    else:
        print(" No hay reservas")

def cancelar_reserva():
    if reservas:
        try:
            print(reservas[0].cancelar())
        except ErrorReserva as e:
            print(f" Error: {e}")
    else:
        print(" No hay reservas")


# ════════════════════════════════════════════════════════════
# PROGRAMA PRINCIPAL
# ════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Seleccione modo de ejecución:")
    print("1. Simulación automática (10 operaciones)")
    print("2. Modo interactivo (menú)")
    opcion = input("Ingrese 1 o 2: ")

    if opcion == "1":
        simulacion_automatica()
    elif opcion == "2":
        while True:
            menu()
            op = input("Ingrese opción: ")
            if op == "1":
                registrar_cliente()
            elif op == "2":
                crear_servicio()
            elif op == "3":
                crear_reserva()
            elif op == "4":
                confirmar_reserva()
            elif op == "5":
                procesar_reserva()
            elif op == "6":
                cancelar_reserva()
            elif op == "7":
                print(" Saliendo del sistema...")
                break
            else:
                print(" Opción inválida")

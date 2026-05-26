import json
from pathlib import Path

from models.usuario import Usuario
from models.reserva import Reserva
from data.vuelos_data import vuelos
from utils.validaciones import (
    pedir_texto,
    pedir_documento,
    pedir_numero_positivo
)

ARCHIVO = Path("reservas.json")


def guardar_reservas(reservas):
    datos = [r.to_dict() for r in reservas]

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_reservas():
    reservas = []

    if not ARCHIVO.exists():
        return reservas

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for r in datos:
        reservas.append(r)

    return reservas


def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")

    nombre = pedir_texto("Nombre: ")
    documento = pedir_documento("Documento: ")

    return Usuario(nombre, documento)


def mostrar_destinos():
    destinos = []

    for vuelo in vuelos:
        if vuelo.destino not in destinos:
            destinos.append(vuelo.destino)

    print("\nDESTINOS DISPONIBLES:")
    for i, destino in enumerate(destinos, start=1):
        print(f"{i}. {destino}")

    opcion = pedir_numero_positivo(
        "Seleccione destino: ",
        minimo=1,
        maximo=len(destinos)
    )

    return destinos[opcion - 1]


def seleccionar_vuelo(destino):
    vuelos_filtrados = [v for v in vuelos if v.destino == destino]

    print("\nVUELOS DISPONIBLES:")
    for i, vuelo in enumerate(vuelos_filtrados, start=1):
        print(f"{i}. {vuelo.codigo} - {vuelo.hora} - ${vuelo.precio:,}")

    opcion = pedir_numero_positivo(
        "Seleccione vuelo: ",
        minimo=1,
        maximo=len(vuelos_filtrados)
    )

    return vuelos_filtrados[opcion - 1]


def elegir_asiento(vuelo):
    print("\nASIENTOS DISPONIBLES")

    for i in range(1, 71):
        if i in vuelo.asientos_ocupados:
            print("[X]", end=" ")
        else:
            print(f"[{i:02}]", end=" ")

        if i % 10 == 0:
            print()

    while True:
        asiento = pedir_numero_positivo(
            "\nSeleccione asiento: ",
            minimo=1,
            maximo=70
        )

        if asiento in vuelo.asientos_ocupados:
            print("Ese asiento ya está ocupado.")
        else:
            vuelo.asientos_ocupados.append(asiento)
            return asiento


def crear_reserva(usuario, reservas):
    destino = mostrar_destinos()
    vuelo = seleccionar_vuelo(destino)
    asiento = elegir_asiento(vuelo)

    reserva = Reserva(usuario, vuelo, asiento)

    reservas.append(reserva)

    guardar_reservas(reservas)

    print("\nRESERVA REALIZADA")
    print(f"Código: {reserva.codigo}")
    print(f"Usuario: {usuario.nombre}")
    print(f"Destino: {vuelo.destino}")
    print(f"Asiento: {asiento}")
    print(f"Total: ${vuelo.precio:,}")


def mostrar_reservas(reservas):
    print("\n--- RESERVAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for i, reserva in enumerate(reservas, start=1):

        if isinstance(reserva, dict):
            print(f"""
Reserva #{i}
Código: {reserva["codigo"]}
Nombre: {reserva["nombre"]}
Destino: {reserva["destino"]}
Hora: {reserva["hora"]}
Asiento: {reserva["asiento"]}
Precio: ${reserva["precio"]:,}
""")
        else:
            print(f"""
Reserva #{i}
Código: {reserva.codigo}
Nombre: {reserva.usuario.nombre}
Destino: {reserva.vuelo.destino}
Hora: {reserva.vuelo.hora}
Asiento: {reserva.asiento}
Precio: ${reserva.vuelo.precio:,}
""")


def cancelar_reserva(reservas):
    mostrar_reservas(reservas)

    if not reservas:
        return

    opcion = pedir_numero_positivo(
        "Seleccione el número de la reserva a cancelar: ",
        minimo=1,
        maximo=len(reservas)
    )

    eliminada = reservas.pop(opcion - 1)

    guardar_reservas(reservas)

    codigo = eliminada["codigo"] if isinstance(eliminada, dict) else eliminada.codigo

    print(f"\nReserva {codigo} cancelada correctamente.")
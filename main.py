from services.reserva_service import (
    registrar_usuario,
    crear_reserva,
    mostrar_reservas,
    cancelar_reserva,
    cargar_reservas,
)

def menu():
    reservas = cargar_reservas()

    while True:
        print("\n==============================")
        print("      QVIAJES AIRLINES")
        print("==============================")
        print("1. Registrar reserva")
        print("2. Ver reservas")
        print("3. Cancelar reserva")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            usuario = registrar_usuario()
            crear_reserva(usuario, reservas)

        elif opcion == "2":
            mostrar_reservas(reservas)

        elif opcion == "3":
            cancelar_reserva(reservas)

        elif opcion == "4":
            print("\nGracias por usar QVIAJES AIRLINES.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
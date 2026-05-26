def pedir_numero_positivo(mensaje, minimo=1, maximo=None):
    while True:
        entrada = input(mensaje).strip()

        if not entrada.isdigit():
            print("Error: solo se permiten números.")
            continue

        valor = int(entrada)

        if valor < minimo:
            print(f"Error: mínimo permitido {minimo}.")
        elif maximo and valor > maximo:
            print(f"Error: máximo permitido {maximo}.")
        else:
            return valor


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()

        if valor == "":
            print("Error: el campo no puede estar vacío.")
        elif any(c.isdigit() for c in valor):
            print("Error: no se permiten números.")
        else:
            return valor


def pedir_documento(mensaje):
    while True:
        valor = input(mensaje).strip()

        if not valor.isdigit():
            print("Error: el documento solo acepta números.")
        else:
            return valor
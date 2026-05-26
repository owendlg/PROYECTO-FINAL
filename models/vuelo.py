import random

class Vuelo:
    def __init__(self, codigo, origen, destino, precio, avion, hora):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.precio = precio
        self.avion = avion
        self.hora = hora
        self.asientos_ocupados = random.sample(range(1, 71), 20)
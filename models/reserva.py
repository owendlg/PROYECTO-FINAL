import random

class Reserva:
    def __init__(self, usuario, vuelo, asiento):
        self.usuario = usuario
        self.vuelo = vuelo
        self.asiento = asiento
        self.codigo = random.randint(1000, 9999)

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.usuario.nombre,
            "documento": self.usuario.documento,
            "destino": self.vuelo.destino,
            "hora": self.vuelo.hora,
            "avion": self.vuelo.avion,
            "asiento": self.asiento,
            "precio": self.vuelo.precio
        }
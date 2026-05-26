from models.persona import Persona

class Usuario(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)
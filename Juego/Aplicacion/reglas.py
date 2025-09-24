from Dominio.Personaje import Personaje

class Regla:
    def crear_jugador(nombre:str) -> Personaje:
        jugador = Personaje(nombre)
        return jugador

    def atacar():
        pass
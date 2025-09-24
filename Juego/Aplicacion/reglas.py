from Dominio.Personaje import Personaje
import random
from Persistencia.gestionNPC import enemigos

class Regla:
    def crear_jugador(nombre:str) -> Personaje:
        jugador = Personaje(nombre)
        return jugador

    def atacar(enemigo):
        exito = random.choice("si","no")
        if exito == "si":
            damage = random.randint(1,40)            
            critico = random.randint(1,2)
            if critico == 1:
                damage *= 2
        else:
            damage = 0

        salud_restante = enemigos.salud - damage
        return salud_restante
    
    def asignar_enemigo() -> Personaje :
        enemigo = random.choice(enemigos)
        nombre = enemigo["nombre"]
        nivel = enemigo["nivel"]
        salud = enemigo["salud"]
        enemigo = Personaje(nombre, nivel, salud)
        return enemigo
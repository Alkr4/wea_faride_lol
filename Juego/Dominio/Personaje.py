import random

class Personaje:
    def __init__(self,nombre:str,nivel:int=1,salud:int=100)-> None: 
        """
        Permite crear objetos de la clase Personaje.
        Parametros:
            nombre:str    -> Corresponde al nombre del personaje.
            nivel:int=1   -> Corresponde al nivel de experiencia del personaje, con valor por defecto 1.
            salud:int=100 -> Corresponde al porcentaje de vida del personaje.
        Retorno:
            Sin retorno.
        """
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud

    def __str__(self)->str:
        return f"{self.nombre} (Nivel: {self.nivel}/Salud: {self.salud}%)"

    def atacar(self,objetivo) -> int:
        exito = random.choice(["si","no"])
        danio = random.randint(1,40)
        if exito == "si":
            objetivo.salud -= danio
            print(f"{self.nombre} ataca a {objetivo.nombre} quitandole {danio}% de vida")
        else:
            print(f"{objetivo.nombre} esquiva a {self.nombre} y le dice ...Juiste Weno!!")
            danio = 0
        return objetivo.salud
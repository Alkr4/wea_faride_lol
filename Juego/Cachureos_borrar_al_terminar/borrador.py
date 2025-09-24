# implementación
def saludar(nombre:str,jornada:str="mañana")->None:
    """
    Función que permite saludar de acuerdo con el nombre 
    y la jornada que se entrega como parametros.
    Params: nombre: str -> Corresponde al nombre para el saludo.
            jornada: str -> Corresponde a la jornada que discrimirara si es mañana, tarde...
    Returns: No retorna nada
    """
    if jornada == "mañana":
        print(f"Buenos días {nombre}")
    elif jornada == "tarde":
        print(f"Buenas tardes {nombre}")
    elif jornada == "noche":
        print(f"Buenas noches {nombre}")
    else:
        print(f"Wena shoro {nombre}")


# la llamada a la función
saludar("Teruka","tarde")
saludar("Rubiesito")


import random

exito = random.choice(["si","no"])
print(exito)
danio = random.randint(1,40)
print(f"daño: {danio}")
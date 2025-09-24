from colorama import Fore,Back,Style
from Aplicacion.reglas import Regla
from Dominio.Personaje import Personaje

def menu_inicio()-> Personaje:
    print(Fore.GREEN)
    nombre = input("Ingrese nombre de su jugador: ")
    jugador = Regla.crear_jugador(nombre)
    print(f"Bienvenido {jugador.nombre}")
    return jugador

def menu_principal(jugador)->None:
    """
    Función que solicita al usuario el número de a 
    opción seleccionada.
    """
    print(Fore.GREEN + "\n *** Menu de Opciones del juego *** ")
    print("-"*50)
    print("1. Atacar")
    print("2. Saludar")
    print("3. Meditar")
    print("0. ")
    print("-"*50)
    opcion = int(input("Seleccione su opción: "))
    
    if opcion==1:
        enemigo = Regla.asignar_enemigo()
        print(f"Te enfrentaras a: {enemigo.nombre} que es nivel {enemigo.nivel} y tiene {enemigo.salud} puntos de salud")
        resultado_ataque = Regla.atacar(enemigo)
        print(f"{jugador.nombre} ataca a {enemigo.nombre} y resulta en {resultado_ataque} puntos de daño")


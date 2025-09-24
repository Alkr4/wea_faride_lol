from colorama import Fore,Back,Style
from Aplicacion.reglas import Regla

def menu_inicio():
    print(Fore.GREEN)
    nombre = input("Ingrese nombre de su jugador: ")
    jugador = Regla.crear_jugador(nombre)
    print(f"Bienvenido {jugador.nombre}")

def menu_principal()->None:
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
        nombre = input("Ingrese nombre de su jugador.")


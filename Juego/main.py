from Modelo.Personaje import Personaje

player1 = Personaje("Mario")
player2 = Personaje("Koopa")

print(player1)
print(player2)

salud_final = player1.atacar(player2)
print(f"Finalmente {player2.nombre} queda con {salud_final}% de vida.")
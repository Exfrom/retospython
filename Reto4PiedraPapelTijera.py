5
from random import randint


maquina=randint(1,3)
jugador=int(input(f"Elige  una opcion:\n 1-piedra\n 2-papel\n 3-tijera:\n"))
print(maquina)
if maquina == jugador:
    print("Empate!!!!!!!")
elif maquina==2 and jugador==3: 
    
    print("Gana Jugador!!!!!!!")
elif maquina==1 and jugador==2:
    print("Gana Jugador!!!!!!!!")
elif maquina==3 and jugador==1:
    print("Gana Jugador!!!!!!!!")
elif jugador==3 and maquina==1:
    print("Gana Maquina!!!!!!!!")
elif jugador==1 and maquina==2:
    print("Gana Maquina!!!!!!!!")
elif jugador==2 and maquina==3:
    print("Gana Maquina!!!!!!!!")
else:
    print("OPCION ERRADA")
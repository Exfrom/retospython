from random import randint
dado1=randint(1,6)
print(f"maquina:\n{dado1}")
dado2=randint(1,6)
print(f"maquina:\n{dado2}")

resultado=(dado1+dado2)

if resultado==2:
    print("ganaste")
elif resultado==3:
    print("ganaste")
elif resultado==11:
    print("ganaste")
elif resultado==2 and resultado==12:
    print("ganaste")
elif resultado==7:
    print("ganaste")
else:
    print("perdiste")
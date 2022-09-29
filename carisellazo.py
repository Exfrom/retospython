from random import randint 
moneda=randint(1,2)
eleccion=int(input("digite 1 para escoger cara o 2 para escoger sello "))
print(moneda)
if moneda==1 and eleccion==1:
    print("Salio cara, Usted escogio cara ganaste!... ")
elif moneda==1 and eleccion==2:
    print("Salio cara, Usted escogio sello perdiste!... ")
elif moneda==2 and eleccion==2:
    print("Salio sello, Usted escogio sello ganaste!... ")
elif moneda==2 and eleccion==1:
    print("Salio sello, Usted escogio cara perdiste!... ")
elif eleccion!=1 or eleccion!=2:
    print("Digitaste una eleccion incorrecta")
else:
    print("datos incorrectos")


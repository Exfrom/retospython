from random import randint 
valorglobal=100000
repetir=int(input("¿Cuantas veces desea jugar: " ))
moneda=randint(1,2)
eleccion=int(input("digite 1 para escoger cara o 2 para escoger sello "))
print(moneda)
for i in range(repetir):
    apostado=int(input("Digita valor apostado "))
    saldo=valorglobal-apostado
if moneda==1 and eleccion==1:
    print("Salio cara, Usted escogio cara ganaste!... ")
    saldo=valorglobal+(apostado*2)
elif moneda==1 and eleccion==2:
    print("Salio cara, Usted escogio sello perdiste!... ")
    saldo=valorglobal-apostado
elif moneda==2 and eleccion==2:
    print("Salio sello, Usted escogio sello ganaste!... ")
    saldo=valorglobal+(apostado*2)
elif moneda==2 and eleccion==1:
    print("Salio sello, Usted escogio cara perdiste!... ")
elif eleccion!=1 or eleccion!=2:
    print("Digitaste una eleccion incorrecta")
    saldo=valorglobal-apostado
else:
    print("datos incorrectos")
     



    
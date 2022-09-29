from random import randint
seguir="s"
total=0
while seguir=="s" or seguir=="S":
    precio=int(input("Ingrese el precio del producto:\n"))
    cantidad=int(input("Ingrese la cantidad del producto:\n"))
    subtotal=precio*cantidad
    total=total+subtotal
    seguir=input("Para ingresar otro producto ingrese S/s o N/n para Terminar\n")
print(f"el valor de la compra es:\n{total}")

print("OPCIONES_SORTEO:\n1.bolita_roja=10%\n2.bolita_azul=30%\n3.bolita_amarilla=50%\n4.bolita:blanca:compragratis \n")

bolitas=randint(1,4) 
print(bolitas)

if total>=50000 and bolitas==1:
      print("felicitaciones ganaste 10% descuento en el valor de tu compra\nvalor final a pagar con descuento es:\n")
      valorfinal=int(input(total-total*0.10))
elif total>=50000 and bolitas==2:
      print("felicitaciones ganaste 30% descuento en el valor de tu compra\nvalor final a pagar con descuento es:\n")
      valorfinal=int(input(total-total*0.30))
elif total>=50000 and bolitas==3:
      print("felicitaciones ganaste 50% descuento en el valor de tu compra\nvalor final a pagar con descuento es:\n")
      valorfinal=int(input(total-total*0.50))
elif total>=50000 and bolitas==4:
      print("felicitaciones te llevas gratis la compra")    
else:
      print("Lo siento no aplica para sorteo")
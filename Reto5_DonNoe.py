from random import randint
valorcompra = int(input("digite el  valor de la compra:\n"))

print("OPCIONES_SORTEO:\n1.bolita_roja=10%\n2.bolita_azul=30%\n3.bolita_amarilla=50%\n4.bolita:blanca:compragratis \n")

bolitas=randint(1,4) 
print(bolitas)

if valorcompra>=50000 and bolitas==1:
      print("felicitaciones ganaste 10% descuento en el valor de tu compra\nvalor final a pagar con descuento es:\n")
      valorfinal=int(input(valorcompra-valorcompra*0.10))
elif valorcompra>=50000 and bolitas==2:
      print("felicitaciones ganaste 30% descuento en el valor de tu compra\nvalor final a pagar con descuento es:\n")
      valorfinal=int(input(valorcompra-valorcompra*0.30))
elif valorcompra>=50000 and bolitas==3:
      print("felicitaciones ganaste 50% descuento en el valor de tu compra\nvalor final a pagar con descuento es:\n")
      valorfinal=int(input(valorcompra-valorcompra*0.50))
elif valorcompra>=50000 and bolitas==4:
      print("felicitaciones te llevas gratis la compra")     
else:
      print("Lo siento no aplica para sorteo")












##sorteo = ['bolita_roja', 'bolita_azul', 'bolita_amarilla', 'bolita_blanca']
##supermercadoNoe = choice(sorteo)
##print("sacaste la bolita:",supermercadoNoe)

##valorcompra = int(input("digite el  valor de la compra:"))
##if supermercadoNoe=='bolita_roja' and valorcompra>=50000:
      ##valorapagar= valorcompra * 0.10
      ##print("El valor a pagar de tu compra con descuento es:", valorapagar)




 





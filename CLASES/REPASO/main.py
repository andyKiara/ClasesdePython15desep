
#1.crear un programa que me pida la edad de una persona si
#la edad es mayor o igual a 18 que me muestre un mensaje 'eres 
#mayor de edad' caso contrario que me muestre un mensaje 'eres menor de edad


edad = int(input("17: "))

if edad >= 18:
   print("Eres mayor de edad.")
else:
   print("Eres menor de edad.")

#2.Una tienda comercial desea hacer un descueto del 20%, crear 
#un programa que me determine si el cliente se hace acreedor del
#descueto teniendo encuenta los siguiente, si el cliente realiza 
#una compra de igual o mayor a 1000 soles mostrar un mensaje que
#diga 'ganaste el descuento del 20% ahora pagaras <mostrar el 
#total de la compra menos el descuento en caso la compra no
#supere los 1000 soles entonces mostrar un mensaje que diga 'no
#aplicas al descuento <mostrar el monto de la compra>'


monto_compra = float(input("Ingrese el monto de la compra en soles: "))

if monto_compra >= 1000:
    descuento = monto_compra * 0.2
    total_con_descuento = monto_compra - descuento
    print("¡Ganaste el descuento del 20%! Ahora pagarás:", total_con_descuento, "soles.")
else:
    print("No aplicas al descuento. El monto de tu compra es:", monto_compra, "soles.")
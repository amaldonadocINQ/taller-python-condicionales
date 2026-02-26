subtotal = float(input("Ingresa el subtotal: "))
tipoCliente = input("Ingresa si eres vip o regular: ")
if tipoCliente.lower() == "vip":
    descuento = 0.15
else:
    if subtotal >= 100:
        descuento = 0.05
    else:
        descuento = 0.00
print (f"El subtotal es: ${subtotal} \nEl descuento aplicado es: {descuento*100}% \nEl total es: ${subtotal - (descuento*subtotal)}")
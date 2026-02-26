n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))
if n1<=100 and n1>=0 and n2<=100 and n2>=0 and n3<=100 and n3>=0:
    promedio = (n1+n2+n3)/3
    if promedio >= 90:
        tipo = "Excelente"
    elif promedio >=80 and promedio<90:
        tipo = "Muy Bueno"
    elif promedio >=70 and promedio<80:
        tipo = "Bueno"
    elif  promedio >=60 and promedio<70:
        tipo = "Supletorio"
    else:
        tipo = "Reprobado"
    print (f"Las notas ingresadas fueron: {n1, n2, n3} \nEl promedio es: {promedio:.2f} \nLa clasificación final es: {tipo}")
else:
    "Error: Alguna nota es inválida"    
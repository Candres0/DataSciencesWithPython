"""Escriba un programa que pida dos números enteros y que calcule su división, 
escribiendo si la división es exacta o no.
DIVISOR DE NÚMEROS
Escriba el dividendo: 14
Escriba el divisor: 5
La división no es exacta. Cociente: 2 Resto: 4
DIVISOR DE NÚMEROS
Escriba el dividendo: 20
Escriba el divisor: 4
La división es exacta. Cociente: 5"""

print("DIVISOR DE NUMEROS")
dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))
if divisor == 0:
    print("No se puede dividir por 0")
else:
    cociente = dividendo//divisor
    resto = dividendo%divisor
    if resto == 0:
        print("La division es exacta. Cociente: " + str(cociente))
    else:
        print("La division no es exacta. Cociente: " + str(cociente) + " Resto: " + str(resto))



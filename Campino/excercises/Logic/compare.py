"""Escriba un programa que pida dos números y que conteste cuál es el menor 
y cuál el mayor o que escriba que son iguales.
COMPARADOR DE NÚMEROS
Escriba un número: 23
Escriba otro número: 14.5
Menor: 14.5; Mayor: 23.0
COMPARADOR DE NÚMEROS
Escriba un número: 5.0
Escriba otro número: 5
Los dos números son iguales."""

print("COMPARADOR DE NUMEROS")
num_1 = float(input("Escriba un numero: "))
num_2 = float(input("Escriba otro numero: "))
if num_1 < num_2:
    print("Menor: "+ str(num_1) + " Mayor: "+ str(num_2))
elif num_1 > num_2:
    print("Menor: "+ str(num_2)+ " Mayor: "+ str(num_1))
else:
    print("Los dos son iguales")

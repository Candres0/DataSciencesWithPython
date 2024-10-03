"""Escriba un programa que pida tres números y que escriba si son 
los tres iguales, si hay dos iguales o si son los tres distintos.
COMPARADOR DE TRES NÚMEROS
Escriba un número: 6
Escriba otro número: 6
Escriba otro número más: 6
Ha escrito tres veces el mismo número."""

print("COMPARADOR DE 3 NUMEROS")
num_1 = float(input("Ingrese un numero: "))
num_2 = float(input("ingrese otro numero: "))
num_3 = float(input("Ingrese el ultimo numero: "))
if num_1 == num_2 == num_3:
    print("Los tres numeros son iguales")
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print("Hay dos numeros iguales")
else:
    print("Todos los numeros son diferentes")
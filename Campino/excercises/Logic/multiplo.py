"""Escriba un programa que pida dos números enteros y 
que escriba si el mayor es múltiplo del menor.
COMPARADOR DE MÚLTIPLOS
Escriba un número: 48
Escriba otro número: 6
48 es múltiplo de 6."""

print("COMPARADOR DE MULTIPLOS")
num_1 = int(input("Escriba un numero: "))
num_2 = int(input("Escriba otro numero: "))
if num_1 == 0 or num_2 == 0:
    print("Ningunos de los dos numeros pueded ser 0")
else:
    if num_1 >= num_2:
        if num_1 % num_2 == 0:
            print(str(num_1) + " es múltiplo de " + str(num_2))
        else:
            print(str(num_1) + " NO es múltiplo de " + str(num_2))
    elif num_2 % num_1 == 0:
        print(str(num_2) + " es múltiplo de " + str(num_1))
    else:
        print(str(num_2) + " NO es múltiplo de " + str(num_1))
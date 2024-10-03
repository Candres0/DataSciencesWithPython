"""Escriba un programa que pida un año y que escriba si es bisiesto o no.

Se recuerda que los años bisiestos son múltiplos de 4, 
pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.

COMPROBADOR DE AÑOS BISIESTOS
Escriba un año y le diré si es bisiesto: 2012
El año 2012 es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100."""

print("COMPROBADOR DE AÑO BISIESTOS")
year = int(input("Escriba un año para saber si es bisiesto: "))
lead = year % 4
lead_1 = year % 100
lead_2 = year % 400
"""print(lead)
print(lead_1)
print(lead_2)"""
if lead == lead_1 & lead == lead_2:
    print("El año " + str(year) + " es un año bisiesto porque es multiplo de 400")
elif lead_1 == lead:
        print("El año "+ str(year) + " no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400")
elif lead == 0:
        print("El año " +str(year) + " es año bisiesto porque es multiplo de 4 sin ser multiplo de 100") 
else:
        print("El año " + str(year) + " no es un año bisiesto")

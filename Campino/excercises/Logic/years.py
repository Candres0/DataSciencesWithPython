print("COMPARADOR DE AÑOS")
fecha_1 = int(input("¿En qué año estamos?: "))
fecha_2 = int(input("Escriba un año cualquiera: "))

if fecha_1 > fecha_2:
    print("Desde el año " + str(fecha_2) + " han pasado " + str(fecha_1 - fecha_2) + " años")
elif fecha_1 < fecha_2:
    print("Para llegar al año " + str(fecha_2) + " faltan " + str(fecha_2 - fecha_1) + " años")
else:
    print("¡Son el mismo año!")
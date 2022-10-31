# Ejercicio 3

número0 = int(input("Ingrese un número entero mayor a 0 "))
número1 = int(input("Ingrese otro número entero mayor a 0 "))

if (número0 == número1):
    print("Los dos números son iguales, el MCM es ", número0)
else:
    i = 2 
    j = 2
    número0Aux = número0
    número1Aux = número1
    while(número0Aux != número1Aux):
        while (número0Aux < número1Aux):
            i += 1
            número0Aux = número0 * i
        while (número0Aux > número1Aux):
            j += 1
            número1Aux = número1 * j
print("El MCM entre " + str(número0) + " y " + str(número1) + " es " + str(número0Aux))



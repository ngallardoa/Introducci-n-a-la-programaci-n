# # Difícil 1:

# string = str(input("Ingresar una frase: "))
# stringSinEspacios = string.replace(" ", "")
# stringAlReves = ""
# longitudString = len(stringSinEspacios)

# while (longitudString >= 1):
#     longitudString -= 1
#     stringAlReves += stringSinEspacios[longitudString]

# longitudString = len(stringSinEspacios)

# if (stringSinEspacios[longitudString - 1] != stringAlReves[longitudString - 1]):
#     print("No son iguales")
# else:
#     longitudString -= 1
#     while (stringSinEspacios[longitudString - 1] == stringAlReves[longitudString - 1] and longitudString > 0):
#         print("longitud: ", longitudString)
#         longitudString -= 1
#         print("longitud después: ", longitudString)
#     if (stringSinEspacios[longitudString - 1] == stringAlReves[longitudString - 1]):
#         print("Son palíndromos")
#     if (stringSinEspacios[longitudString - 1] != stringAlReves[longitudString - 1]):
#         print("No son palíndromos")

# # Arnaldo pasa por una concesionaria para averiguar por un Fiat 600 0 km. Él posee una cantidad de dinero disponible para comprarlo. Si el auto sale menos de lo que tiene lo compra directamente. Si no, si le alcanza aunque sea para la mitad paga todo lo tenga y la concesionaria le financia lo faltante con un %10 de recargo. Arnaldo accede a este préstamo si el dinero que tiene que agregar no supera los $10000. Se pide hacer un programa que diga que va a realizar Arnaldo y en caso de comprar indique cuanto paga en total.

# dineroDisponible = int(input("Ingrese el dinero disponible: "))
# precioAuto = int(input("Ingrese el precio del auto: "))

# if (dineroDisponible >= precioAuto):
#     print("Arnaldo paga el total")
# if (dineroDisponible < precioAuto):
#     tasaFinanciamiento = 0.1
#     capitalFinanciado = (precioAuto - dineroDisponible)* (1.0 + tasaFinanciamiento)
#     if (dineroDisponible > (precioAuto / 2) and capitalFinanciado <= 10000):
#         print("Arnaldo se financia con: ", capitalFinanciado)
#         print("Arnaldo paga: ", dineroDisponible)
#     else:
#         print("Arnaldo no puede comprar el auto")

i = 1
miLista = ["perro","gato","gato"]
tuLista = ["gato","perro","perro"]

for i in range (len(miLista)):
    if miLista[i] != "perro":
        print("miau")
    print("guau")
print(tuLista[i])
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

# Difícil 2:

string = str(input("Ingresar una frase: "))
vocales = "aeiou"
índice = 0
palabra = ""
vocalesEnString = 0
carácteres = 0
# vocal = 0

while (string == ""):
    string = str(input("Ingresaste una frase vacía. Ingresar una frase: "))

while (índice < len(string)):
    while (string[índice] != " "):
        carácteres += 1
        for vocal in vocales:
            if (string[índice] == vocal):
                vocalesEnString += 1
        palabra += string[índice]
        índice += 1
    print("La palabra " + str(palabra) + " tiene: " + str(carácteres) + " letras y " + str(vocalesEnString) + " vocales.")
    print("Índice es: ", índice)
    palabra = ""
    vocalesEnString = 0
    carácteres = 0
    índice += 1
    print("Índice después es: ", índice)
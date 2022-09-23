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


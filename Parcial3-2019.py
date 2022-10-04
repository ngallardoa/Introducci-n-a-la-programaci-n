from random import *

stringAAnalizar = input("Ingrese una palabra: ")
stringAAnalizarSinPrimerCaracter = ""
string1 = ""
string2 = ""
caracteresRepetidos0 = stringAAnalizar[0]
caracteresRepetidos1 = ""
i = 1

while (i < len(stringAAnalizar)):
    stringAAnalizarSinPrimerCaracter += stringAAnalizar[i]
    i += 1

i = 0

while (i < len(stringAAnalizar)): # ciclo para asignar cada una de las letras a los strings
    if stringAAnalizar[i] in caracteresRepetidos0:
        caracteresRepetidos1 += stringAAnalizar[i]
    else:
        if (randrange(2) == 0):
            string1 += stringAAnalizar[i]
        else:
            string2 += stringAAnalizar[i]
        caracteresRepetidos0 += stringAAnalizar[i]
    i += 1

caracteresRepetidos0 = ""

if caracteresRepetidos1[0] not in stringAAnalizarSinPrimerCaracter: # como la primera letra del string ingresado por el usuario nunca se analizó si se repite, este ciclo realiza esta operación, y en caso de no estar repetido, lo elimina del string caracteresRepetidos0 (el string que guarda los caracteres repetidos) e imprime este.
    for i in range(1, len(caracteresRepetidos1)): 
        caracteresRepetidos0 += caracteresRepetidos1[i]
    print("Los caracteres repetidos son: ", caracteresRepetidos0)
    print("string1", string1)
    print("string1", string2)
else:
    print("Los caracteres repetidos son: ", caracteresRepetidos1)
    print("string1", string1)
    print("string1", string2)

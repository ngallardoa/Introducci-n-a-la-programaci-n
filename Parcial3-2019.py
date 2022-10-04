from random import *

stringAAnalizar = input("Ingrese una palabra: ")
string0 = ""
string1 = ""
caracteresRepetidos0 = ""
caracteresRepetidos1 = ""
i = 1

if (randrange(2) == 0): # Asigna el primer caracter del string de forma pseudoaleatoria a alguno de los substrings
    string0 += stringAAnalizar[0]
else:
    string1 += stringAAnalizar[0]

while (i < len(stringAAnalizar)): # Ciclo para asignar cada una de las letras a los substrings de forma pseudoaleatoria
    print(stringAAnalizar[i])
    if stringAAnalizar[i] in caracteresRepetidos0 or stringAAnalizar[i] == stringAAnalizar[0]:
        caracteresRepetidos1 += stringAAnalizar[i]
    else:
        if (randrange(2) == 0):
            string0 += stringAAnalizar[i]
        else:
            string1 += stringAAnalizar[i]
        caracteresRepetidos0 += stringAAnalizar[i]
    i += 1

difLen = len(string0) - len(string1)

if (difLen < 0): # Si string0 es más corto que string1, entra en este condicional para completarlo con "&" hasta igualar longitudes
    while (difLen != 0):
        string0 += "&"
        difLen += 1
if (difLen > 0): # Si string1 es más corto que string0, entra en este condicional para completarlo con "$" hasta igualar longitudes
    string1Auxiliar = ""
    while (difLen != 0):
        string1Auxiliar += "$"
        difLen -= 1
    string1Auxiliar += string1
    string1 = string1Auxiliar

print("Los caracteres repetidos son: ", caracteresRepetidos1)
print("string0", string0)
print("string1", string1)

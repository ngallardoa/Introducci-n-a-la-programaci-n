from principal import *
from configuracion import *
import random
import math

archivo = open("lemario.txt","r")

def nuevaPalabra(lista):
    númeroRandom = random.randrange(len(lista))
    return lista[númeroRandom]

def lectura(archivo, salida, largo):
    largoReal = largo + 1
    for linea in archivo.readlines():
        if len(linea) == largoReal:
            salida.append(linea)
    return salida    

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if palabra == palabraCorrecta:
        return True
    if palabra != palabraCorrecta:
        i = 0
        while i < len(palabra):
            if palabra[i] == palabraCorrecta[i]:
                correctas.append(palabra[i])
            else:
                if palabra[i] in palabraCorrecta:
                    casi.append(palabra[i])
                else:
                    incorrectas.append(palabra[i])
            i += 1
        return False

def corregirPalabraCorrecta(string):
    string0 = ""
    for i in range (0, len(string)-1):
        string0 += string[i]
    string = string0
    return string

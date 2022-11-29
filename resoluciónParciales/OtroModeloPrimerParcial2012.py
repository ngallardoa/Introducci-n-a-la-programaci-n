# Ejercicio 3

# número0 = int(input("Ingrese un número entero mayor a 0 "))
# número1 = int(input("Ingrese otro número entero mayor a 0 "))

# if (número0 == número1):
#     print("Los dos números son iguales, el MCM es ", número0)
# else:
#     i = 2 
#     j = 2
#     número0Aux = número0
#     número1Aux = número1
#     while(número0Aux != número1Aux):
#         while (número0Aux < número1Aux):
#             i += 1
#             número0Aux = número0 * i
#         while (número0Aux > número1Aux):
#             j += 1
#             número1Aux = número1 * j
# print("El MCM entre " + str(número0) + " y " + str(número1) + " es " + str(número0Aux))

# def esPrimo(número):
#     if (número < 1):
#         return -1
#     if (número == 1):
#         return True
#     for i in range (2, número):
#         if (número % i == 0):
#             return False
#     return True

# # booleano = esPrimo(int(input("Ingrese un número: ")))
# # print(booleano)


# def cuántosPrimosHacenFalta(número):
#     contadorPrimos = 0
#     sumatoriaPrimos = 0
#     for i in range (1, número):
#         print("Sumatoria es: ", sumatoriaPrimos)
#         print("i es: ", i)
#         if (esPrimo(i) == True) and (sumatoriaPrimos < número):
#             contadorPrimos += 1
#             sumatoriaPrimos += i
#     return contadorPrimos

# preguntarNúmero = cuántosPrimosHacenFalta(int(input("Ingrese un número mayor a 1: "))) 
# print("Hacen falta", preguntarNúmero, "primos")

# def sugerirAmigos(nombreLista0, lista0, nombreLista1, lista1):
#     listaSugerencia = []
#     listaMenosContactos = ""
#     i = 0
#     if (len(lista0) > len(lista1)):
#         listaMenosContactos += nombreLista1
#         while (i < len(lista0)):
#             if lista0[i] not in lista1:
#                 listaSugerencia.append(lista0[i])
#             i += 1
#     if (len(lista0) < len(lista1)):
#         listaMenosContactos += nombreLista0
#         while (i < len(lista1)):
#             if lista1[i] not in lista0:
#                 listaSugerencia.append(lista1[i])
#             i += 1
#     return listaSugerencia, listaMenosContactos

# lista1 = [5, 10, 8, 9, 6, 7, 5, 3, 10]
# lista2 = [6, 9, 1, 6, 9, 2, 7, 7, 8, 15, 22]

# def combinarLista(lista0, lista1, número):
#     listaFinal = []
#     i = 0
#     if (len(lista0) < len(lista1)):
#         while(i < len(lista0)):
#             if ((lista0[i] + lista1[i]) > número and (lista0[i] + lista1[i]) not in listaFinal):
#                 listaFinal.append(lista0[i] + lista1[i])
#             i += 1
#     if (len(lista1) < len(lista0)):
#         while(i < len(lista1)):
#             if ((lista0[i] + lista1[i]) > número and (lista0[i] + lista1[i]) not in listaFinal):
#                 listaFinal.append(lista0[i] + lista1[i])
#             i += 1
#     return listaFinal

# lista = combinarLista(lista1, lista2, 14)
# print(lista)


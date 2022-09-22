# # """
# # def preguntarNombre ():
# #     x = input ("Ingrese el primer valor")
# #     y = input ("Ingrese el segundo valor")
# #     z = input ("Ingrese el tercer valor")
# #     print("El primer valor es " + x," El segundo valor es " + y," El tercer valor es " + z)

# # preguntarNombre()
# # """

# a = 0
# b = 0
# c = 0

# def pedirCoeficientes():
#     a = int(input("ingrese el valor de a"))
#     b = int(input("ingrese el valor de b"))
#     c = int(input("ingrese el valor de c"))
#     print("Los valores ingresados son",a,b,c)
#     consultarValores = int(input("Son correctos los valores? En caso de ser así, presione 0. Caso contrario presione 1"))
    
#     if consultarValores == 0:
#         print("blabla")

#     elif consultarValores == 1:
#         a = int(input("ingrese el valor de a"))
#         b = int(input("ingrese el valor de b"))
#         c = int(input("ingrese el valor de c"))
    
#     else:
#         print("Introdujo un valor incorrecto")

# def calcularRaíces(coefA,coefB,coefC):
#     x = coefA + coefB + coefC

# def resolvente():
#     pedirCoeficientes()
#     calcularRaíces(a,b,c)

# resolvente()
# import math

# m = int(input("Ingrese un número "))
# n = int(input("Ingrese otro número "))
# print("Los números ingresados son: ", m, n)
# número1 = m
# número2 = n
# dif = int(math.fabs(m - n))
# dif1 = dif + 1
# if (m > n):
#     for l in range(dif1):
#         dif1 = dif + 1 - l
#         número2 = n
#         if (l == 0):
#             for k in range(0, dif1):
#                 print(número1, número2)
#                 número2 = número2 + 1
#         else:       
#             número1 = número1 - 1
#             for k in range(0, dif1):
#                 print(número1, número2)
#                 número2 = número2 + 1
# elif (m < n):
#     for l in range(dif1):
#         dif1 = dif + 1 - l
#         número1 = m 
#         if (l == 0): 
#             for k in range(0, dif1):
#                 print(número1, número2)
#                 número1 = número1 + 1 
#         else:       
#             número2 = número2 - 1
#             for k in range(0, dif1):
#                 print(número1, número2)
#                 número1 = número1 + 1  
# else:
#     número1 = m
#     número2 = n
#     print(número1)
#     print(número2)

# n = int(input("Ingrese el número "))
# i = 1
# acumSuma = 0
# while (i <= n):
#     acumSuma = acumSuma + i
#     i = i + 2
# print(acumSuma)

# n = int(input("Ingrese el número "))
# i = 1
# acumSuma = 1
# total = 0
# print(acumSuma)
# while (i < n):
#     i = i + 1
#     acumSuma = acumSuma + 2
#     print(acumSuma)
#     total = total + acumSuma
# print("El total es: ", total)

# testResults = [ True, True, True, True, False, True ]

# resultado = ""

# for índice in testResults:
#     if (testResults[índice] == "False"):
#         resultado = índice
#         print(resultado)

# print(resultado)





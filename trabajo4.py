# Ejercicio No. 4:
#Escriba una función que reciba una lista y devuelva el total de numeros positivos que contiene.

import random

def contar_positivos(lista):
    if lista:
        positivos = 0
        for i in lista:
            if i >0:
                positivos = positivos + 1
        return positivos
    else:
        return "dato no valido. lista vacia"
    

longitud = random.randint(1, 100)
numeros = [random.randint(-100, 100)for _ in range(longitud)]

resultado = contar_positivos(numeros)
print(numeros)
print("los numeros positivos son: ", resultado)
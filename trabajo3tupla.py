# programa de python que lee y escoge los ultimos valores 

def obtener_primer_ultimo(lista):
    if lista:
        if(len(lista)>=2):
            return  (lista[0], lista[-1])
        else:
            return "la lista no tiene elementos suficientes"
    else:
        return "Dato no valido. lista vacia"

lista_1 = [1,1,1,11,1,111]
resultado = obtener_primer_ultimo(lista_1)
print(resultado)
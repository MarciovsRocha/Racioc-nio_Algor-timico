def soma_positivos(lista):
    soma = 0
    for i in range(0,len(lista)):
        if lista[i] >= 0:
            soma += lista[i]
    return soma

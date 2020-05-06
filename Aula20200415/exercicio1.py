def listaImpar(lim: int):
    i = 0
    lista = []
    while (i<=lim):
        if (i % 2 != 0):
            lista.append(i)
        i+=1
    return lista

limite = 100
array = []
array = listaImpar(limite)
print(array)
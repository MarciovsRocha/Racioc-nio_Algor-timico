def dobro_triplo(lista):
    l_ret = []
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            l_ret.append(2 * lista[i])
        else:
            l_ret.append(3 * lista[i])
    return l_ret

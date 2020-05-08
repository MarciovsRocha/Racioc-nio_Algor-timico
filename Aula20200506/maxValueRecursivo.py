def maximo(v):
    # criterio de parada
    # existir apenas 1 valor na lista
    if (len(v) == 1):
        return v[0]
    # calcular o maximo restante da lista
    max_rest = maximo(v[1:])
    # verificando se a cabeca eh o maior valor
    if (v[0] > max_rest):
        return v[0]
    # o maior valor veio do restante da lista
    else:
        return max_rest
print(maximo([1,2,3,4]))
print(maximo([1000,299,312,43]))
print(maximo([145,23,3123,4232]))

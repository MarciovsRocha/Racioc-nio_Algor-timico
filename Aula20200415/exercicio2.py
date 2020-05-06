def multiplos(x):
    lista = []
    for i in range(1,x):
        if((i % 3 == 0) and (i % 5 == 0)):
            lista.append(i)
    return lista

limite = int(input("Digite um numero: "))
array = []
array = multiplos(limite)
print(f'os multiplos de 3 && 5 sao: {array}')
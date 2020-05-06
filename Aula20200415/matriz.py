matriz = [[0,0,0],[0,0,0],[0,0,0]]

def alimentaMatriz(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            num = int(input(f"Digite um valor para[{i},{j}]"))
            matriz[i][j] = num

def somaAcimaDiagonal(matriz):
    elementos = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            #print(f'[{matriz[i][j]}]', end='')
            if (j >= i):
                elementos += matriz[i][j]
    return elementos

alimentaMatriz(matriz)
soma = somaAcimaDiagonal(matriz)
print(f'a soma eh: {soma}')



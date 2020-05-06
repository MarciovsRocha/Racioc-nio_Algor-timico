matriz = [[0,0,0],[0,0,0],[0,0,0]]

def alimentaMatriz(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            num = int(input(f"Digite um valor para[{i},{j}]"))
            matriz[i][j] = num

def somaAcimaDiagonal(matriz):
    elementos = 0
    elementos2 = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            #print(f'[{matriz[i][j]}]', end='')
            if (j >= i):
                elementos += matriz[i][j]
            if (j > i):
                elementos2 += matriz[i][j]
            
    return elementos,elementos2

alimentaMatriz(matriz)
soma = []
soma = somaAcimaDiagonal(matriz)
print('Contando com os valores da diagonal principal')
print(f'a soma eh: {soma[0]}')
print('Sem Contar com os valores da diagonal principal')
print(f'a soma eh: {soma[1]}')

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
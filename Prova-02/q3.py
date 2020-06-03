def aloca_matriz(n,m):
    if ((n <=0) or (m<=0)):
        return nil
    matriz = []
    for i in range(0,n):
        linha = []
        for j in range(0,m):
            if (i == j):
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha.copy())
    return matriz

def showMatriz(m):
    for i in range(0,len(m)):
        print('|',end='')
        for j in range(0,len(m[i])):
            print(f' {m[i][j]} |',end='')
        print()

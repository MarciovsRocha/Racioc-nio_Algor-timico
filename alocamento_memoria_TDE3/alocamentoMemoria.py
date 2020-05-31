# criando a matriz
memoria = []

# ---------------------------------------------------------------------------------------------------------------------------------------
# funcao para criar a 'memoria'
def criaMatriz(Xmem,Ymem: int):
    if ((Xmem <= 0) or (Ymem <=0)):
        print('Os valores nao podem ser menores ou iguais a zero')
        return 0
    X = []
    memAloc = []
    i = 0
    while i < Ymem:
        X.append(False)
        i += 1
    i = 0
    while i < Xmem:
        memAloc.append(X)
        i += 1
    showMemoria(memAloc)
# ---------------------------------------------------------------------------------------------------------------------------------------
# visualizacao da matriz
def showMemoria(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if (matriz[i][j] == True):
                print(' X |', end='')
            else:
                print(' |', end='')
            #print(f'[{matriz[i][j]}]', end='')
        print()

# ---------------------------------------------------------------------------------------------------------------------------------------
# first fit

# ---------------------------------------------------------------------------------------------------------------------------------------
# best fit

# ---------------------------------------------------------------------------------------------------------------------------------------
# worst fit

# ---------------------------------------------------------------------------------------------------------------------------------------


print('Digite o tamanho da memoria (X,Y) \n sendo X = linhas e Y = colunas') 
qtdeLinhas = int(input('X: '))
qtdeColunas = int(input('Y: '))
print(f'criando uma memoria com tamanho({qtdeLinhas},{qtdeColunas})')
criaMatriz(qtdeLinhas,qtdeColunas)
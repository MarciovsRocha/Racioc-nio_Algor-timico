# importado metodo utilizado no clear()
from os import system

# criando a matriz
memoria = []

# ---------------------------------------------------------------------------------------------------------------------------------------
# metodo para limpar o console
clear = lambda: system('cls')

# ---------------------------------------------------------------------------------------------------------------------------------------
# funcao para criar a 'memoria'
def createMemory(Xmem,Ymem: int):
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
        memAloc.append(X.copy())
        i += 1
    return memAloc

# ---------------------------------------------------------------------------------------------------------------------------------------
# funcao para printar a memoria e seus espacos alocados com X
def showMemory(matriz):
    for i in range(0,len(matriz)):
        print('|',end='')
        for j in range(0,len(matriz[i])):
            if (matriz[i][j] == True):
                print(' X |', end='')
            else:
                print('   |', end='')
        print()

# ---------------------------------------------------------------------------------------------------------------------------------------
# funcao para alocar valores na memoria
def alocMemory(X,Y,memory):
    if (len(X) != len(Y)):
        print('Houve algum erro :( \n tente novamente mais tarde.')
        return -1
    for i in range(0,len(X)):
        memory[X[i]][Y[i]] = True
    return memory

# ---------------------------------------------------------------------------------------------------------------------------------------
# funcao para desalocar valores na memoria
def desalocMemory(qtde, posInit: int, memory):
    count = 0
    for i in range(0,len(memory)):
        if (count == posInit):
            x = i-1
            y = j
            break
        for j in range(0,len(memory[i])):
            count += 1
    print()
    
# ---------------------------------------------------------------------------------------------------------------------------------------
# first fit
def firstFitAloc(aloc: int, memory):
    count = 0
    posX = []
    posY = []
    for i in range(0,len(memory)):
        for j in range(0,len(memory)):
            if (count == aloc):
                memoria = alocMemory(posX,posY,memory)
                return memoria
            elif (memory[i][j] == True):
                count = 0
                posX.clear()
                posY.clear()
            elif (memory[i][j] == False):
                count += 1
                posX.append(i)
                posY.append(j)

# ---------------------------------------------------------------------------------------------------------------------------------------
# best fit

# ---------------------------------------------------------------------------------------------------------------------------------------
# worst fit

# ---------------------------------------------------------------------------------------------------------------------------------------

clear()
print('Digite o tamanho da memoria (X,Y) \n sendo X = linhas e Y = colunas') 
qtdeLinhas = int(input('X: '))
qtdeColunas = int(input('Y: '))
print(f'\n criando uma memoria com tamanho({qtdeLinhas},{qtdeColunas})')
memoria = createMemory(qtdeLinhas,qtdeColunas)
showMemory(memoria)
print()
print()
memoria = firstFitAloc(15,memoria)
showMemory(memoria)
print()
print()
memoria = firstFitAloc(5,memoria)
showMemory(memoria)
print()
print()
memoria = firstFitAloc(40,memoria)
showMemory(memoria)
print()
print()
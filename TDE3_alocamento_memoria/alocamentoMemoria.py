# importado metodo utilizado no clear()
from os import system
import time

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
    verPos = True
    for i in range(0,len(memory)):
        for j in range(0,len(memory[i])):
            if ((count == posInit) and (verPos == True) ):
                count = 0
                verPos = False
            elif ((count < posInit) and (verPos == True)):
                count += 1
            elif ((count <= qtde) and (verPos == False)):
                memory[i][j] = False
                count += 1
            elif ((count > qtde) and (verPos == False)):
                return memory
    
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
def bestFitAloc(aloc: int, memory):
    count = 0
    posX = []
    posY = []
    for i in range(0,len(memory)):
        for j in range(0,len(memory[i])):
            if (count == aloc):
                return 0
            elif (memory[i][j] == True):
                count = 0

            elif (memory[i][j] == False):
                count += 1
                posX.append(i)
                posY.append(j)

# ---------------------------------------------------------------------------------------------------------------------------------------
# worst fit
def WorstFit(matriz,n,teste=False):
    inicio=time.localtime()
    n=int(n)
    local=[]
    compara=[]
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c]==0:
                compara.append([l,c])
                if len(compara)>len(local):
                    local=compara.copy()
            else:
                compara=[]
    if len(local)>=n:
        for i in range(n):
            a=local[i][0]
            b=local[i][1]
            matriz[a][b]=1
        if teste==True:
            erros=0
            sucessos=1
            return matriz,erros,sucessos,inicio.tm_sec
    else:
        if teste==True:
            erros=1
            sucessos=0
            return matriz,erros,sucessos,inicio.tm_sec
    print('\n')
    return menu(matriz)

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
memoria = firstFitAloc(5,memoria)
memoria = firstFitAloc(40,memoria)
showMemory(memoria)
print()
print()
memoria = desalocMemory(4,3,memoria)
memoria = desalocMemory(1,10,memoria)
memoria = desalocMemory(3,0,memoria)
memoria = desalocMemory(6,30,memoria)
showMemory(memoria)
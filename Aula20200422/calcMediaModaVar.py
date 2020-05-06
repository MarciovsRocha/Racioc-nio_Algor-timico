# escrever um algoritmo que leia uma matriz de ordem n por m
# para cada coluna calcule a média, moda e variância dos valores informados
# <<< UTILIZE FUNÇÕES AUXILIARES >>>
Matriz = []
def criaMatriz(i,j, Matriz):
    n_colunas = []
    for y in range(i):
        Matriz.append([input(f"Digite o valor para [{y}][{z}]")for z in range(j)])

def calcMedia(matriz):
    # variaveis a serem utilizadas
    lista = [] # variavel generica de lista
    result = [] # variavel utilizada para armazenar o resultado e retorna-lo
    rows = int(len(matriz)) # numero de linhas
    columns = int(len(matriz[0])) # numero de colunas
    ic = 0 # iterador de colunas
    ir = 0 # iterador de linhas
    # / variaveis a serem utilizadas
    for ic in range(0,len(matriz[0])):
        while ir < rows:
            lista.append(matriz[ir][ic])
            ir += 1 
        print(lista)
        result.append((sum(lista)/(columns-1)))
        ic += 1
    return result
        
    
i = int(input('Digite a qtde de linhas: '))
j = int(input('Digite a qtde de colunas: '))

criaMatriz(i,j,Matriz)

for h in range(0,len(Matriz)):
    for w in range(0,len(Matriz[h])):
        print(f'[{Matriz[h][w]}]', end = '')
    print('')

#print(calcMedia(Matriz))

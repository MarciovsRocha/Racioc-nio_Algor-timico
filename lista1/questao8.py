# faca um algoritimo que receba as coordenadas de dois pontos P1 = (x1,y1) e P2 = (x2,y2), 
# e retorne a distancia euclidiana entre eles.
# ================================================================================================================================
import math
import os # biblioteca importada para executar o comando de limpar a tela
x = [] # definindo a lista de valores do eixo 'x'
y = [] # definindo a lista de valores do eixo 'y'
i = 1 # contador para percorrer os valores dos pontos
adicionarPonto = 's' # definindo o valor de validador da opção para adicionar pontos

# procedimento para limpar o terminal, sempre que precisar limpar o termial deve-se chamar clear()
clear = lambda: os.system('cls')
#clear()

# funcao para adicionar pontos no plano
def adicionaPonto(i):
    x.append(float(input(f"Digite o valor do eixo 'X' para a coordenada do ponto {i}: ")))
    y.append(float(input(f"Digite o valor do eixo 'Y' para a coordenada do ponto {i}: ")))
    #clear()

# funcao para calcular a distancia euclidiana entre 2 pontos
def calculaDistancia(x1,y1,x2,y2: float):
    d = math.sqrt((y2-y1)**2 + (x2-x1)**2) # formula usada para calcular a distancia euclidiana entre 2 pontos
    return d

# verifica se eh a primeira vez que ira adicionar um ponto e por isso ele adiciona o primeiro ponto aqui e depois chama a funcao generica
if i == 1:
    x.append(float(input(f"Digite o valor do eixo 'X' para a coordenada do ponto {i}: "))) 
    y.append(float(input(f"Digite o valor do eixo 'Y' para a coordenada do ponto {i}: "))) 
    #clear()

# loop para adicionar [n] pontos
while ((adicionarPonto == 's') or (adicionarPonto == 'S')):
    i += 1
    adicionaPonto(i)
    adicionarPonto = input("Deseja adicionar outro ponto no plano? [s]im ou [n]ao:  ")
    #clear()
# exibe a lista de pontos e seus valores
print("Selecione dois pontos abaixo para poder calcular a disância entre eles:")
totalPontos = len(x)
i = 0
while i < totalPontos: 
    print(f"Ponto {i+1}, coordenadas: X:{x[i]} Y:{y[i]}") # soma 1 na posicao pois a lista comeca em 0
    i += 1
# 'e1' e 'e2' representam respectivamente a escolha do ponto 1 e do 2ndo ponto
e1 = int(input("Ponto: "))
e2 = int(input("Ponto: "))
print(f"ponto{e1}= X:{x[e1-1]} Y:{y[e1-1]}")
print(f"ponto{e2}= X:{x[e2-1]} Y:{y[e2-1]}")

distancia = calculaDistancia(x[e1-1],y[e1-1],x[e2-1],y[e2-1])
print(f"A distancia entre os pontos {e1} e {e2} eh: {distancia}")

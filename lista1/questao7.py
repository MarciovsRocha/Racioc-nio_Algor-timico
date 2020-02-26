# faca um algoritmo que receba o valor do raio de uma esfera
# e retorne seu volume e area superficial
# =======================================================================================================
 
# definindo o valor da constante pi
pi = 3.1415

# funcao para calcular o volume da esfera
def calculaVolume(r, pi: float):
    V = (pi*(4/3 * (r**3)))
    return V

# funcao para calcular a area superficial da esfera
def calculaAreaSuperficial(r, pi: float):
    S = (4 * pi * (r**2))
    return S

while True:
    # criando menu de escolhas para o usuario
    print("Escolha uma opcao:")
    print("1 - Calculalr o Volume")
    print("2 - Calcular a Area")
    escolha = int(input("Escolha: ")) # variavel para receber o valor da escolha do usuario
    # condicional para verificar se a escolha eh valida
    if ((escolha < 1) or (escolha > 2)):
        print(f"Você entrou com uma opção errada, favor verificar: {escolha}")
    else:
        print("Lembre-se de conferir as unidades de medidas!")
        r = float(input("Digite o valor do raio: ")) # a variavel r representa o raio inserido pelo usuario
        # verifica se o valor inserido para o raio eh compativel
        if r <= 0: 
            print(f"Você entrou com um valor incorreto, favor verificar: {r}")
        elif escolha == 1: # caso escolha seja igual a 1, calcula o volume e imprime na tela
            v = calculaVolume(r,pi)
            print(f"O Volume da Esfera eh: {v}")
        elif escolha == 2: # caso escolha seja igual a 2, calcula o volume e imprime na tela
            s = calculaAreaSuperficial(r,pi)
            print(f"A Area superficial da esfera eh: {s}")
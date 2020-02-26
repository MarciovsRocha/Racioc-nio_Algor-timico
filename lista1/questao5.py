# faca um programa que receba 3 valores a, b e c que representam os lados de um triangulo, 
#  e retorne a sua area , use a formula de herao onde p eh o semi-perimetro
# ======================================================================================
import math

# funcao para calcular o semi-perimetro
def semiPerimetro(a,b,c: float):
    return float((a+b+c)/2)
    
# funcao para calcular a area do triangulo
def calculaArea(a,b,c: float):
    p = semiPerimetro(a,b,c)
    A = float(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    return A

a = float(input("Digite o valor de um lado do triangulo: "))
b = float(input("Digite o valor de outro lado do triangulo: "))
c = float(input("Digite o valor do último lado do triangulo: "))
# condicional para verificar se o valor inserido pelo usuario eh 
if ((a <= 0) or (b <= 0) or (c <= 0)):
    print(f"Voce entrou com algum valor errado, favor verifique os valores inseridos e arurme.")
    print(f"Valor do 1 lado:{a}")
    print(f"Valor do 2 lado:{b}")
    print(f"Valor do 3 lado:{c}")
else:
    print(f"O valor da area do triangulo eh: {calculaArea(a,b,c,)}.") 
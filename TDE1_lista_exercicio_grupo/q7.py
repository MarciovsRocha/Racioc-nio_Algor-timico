# q7.py: Construir um algoritmo para calcular as raízes de uma equação do 2o grau, sendo
# que os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário através do
# teclado. Caso não existam reais, o usuário deverá ser informado. 

a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

def eq_2_grau(a,b,c):
    delta = b**2-4*a*c
    if delta < 0:
        print("Delta negativo: " + str(delta))
        return
    raiz1 = (-b + (delta)**(1/2))/(2*a)
    raiz2 = (-b - (delta)**(1/2))/(2*a)
    print("Primeira raiz: " + str(raiz1) +"\nSegunda raiz: " + str(raiz2))

eq_2_grau(a,b,c)
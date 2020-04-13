# Dado três valores A, B e C, construa um algoritmo para verificar se estes 
# valores podem ser valores dos lados de um triângulo, e se for, determine 
# se é um triângulo escaleno, equilátero, ou isósceles.
def condicaoExistencia(a,b,c: float):
#           1 condicao              2 condicao               3 condicao   
    if ( ((b-c) < a < (b+c)) and ((a-c) < b < (a+c)) and ((a-b) < c < (a+b)) ):
        return True
    else:
        return False

def tipoTriangulo(a,b,c: float):
    if ( (a != b) and (a != c) and (b != c) ):
        print("Este eh um triangulo escaleno")
    elif ( ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a)) ):
        print("Este eh um triangulo Isoceles")
    elif( (a == b) and (a == c) ):
        print("Este eh um triangulo Isoceles")
    else:
        print("Algo deu errado :(, tente novamente")

a = float(input("Digite o valor de 1 lado do triangulo: "))
b = float(input("Digite o valor do outro lado do triangulo: "))
c = float(input("Digite o valor do ultimo do triangulo: "))

if (condicaoExistencia(a,b,c) == True):
    tipoTriangulo(a,b,c)
else:
    print("Nao eh possivel construir um triangulo com esses valores, tente novamente com valores diferentes.")
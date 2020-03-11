lista = []
def comparaNumeros(n1,n2,n3: int):
    if (n1 < n2):
        if (n2 < n3) and (n1 < n3):
            lista.append(n1)
            lista.append(n2)
            lista.append(n3)
        else:
            lista.append(n1)
            lista.append(n3)
            lista.append(n2)
    else:
        if (n1 < n3) and (n2 < n3):
            lista.append(n2)
            lista.append(n1)
            lista.append(n3)
        else:
            lista.append(n3)
            lista.append(n2)
            lista.append(n1)

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
comparaNumeros(num1,num2,num3)
print(lista)
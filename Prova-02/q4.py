def calcFibonacci(n):
    anterior = 0
    proximo = 0
    lista = []
    for i in range(n):
        lista.append(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1
    return lista

n = int(input("Digite o n-esimo termo da sequencia de fibonacci"))
fibonacci = []
fibonacci = calcFibonacci(n)
print(fibonacci)

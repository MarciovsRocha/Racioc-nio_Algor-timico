def calcFatorial(n: int):
    resultado = 1
    i = 1
    while i < n:
        resultado *= i
        i += 1
    return resultado


x = int(input('Digite um numero para calcular o fatorial: '))
print(f'!{x} = {calcFatorial(x)}')

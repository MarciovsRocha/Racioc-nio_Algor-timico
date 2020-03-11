def adicao(a,b: int):
    if(type(a) != int) or type(b) != int:
        print("Valor inserido incorreto")
    else:
        s = a+b
        if s > 20.0:
            s = s + 8.0
        else:
            s = s - 5.0
    return s

a = int(input("Digite o valor do primeiro numero: "))
b = int(input("Digite o valor do segundo numero: "))
print(f"Resultado: {adicao(a,b)}")

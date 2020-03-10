def adicao(a,b: float):
    if(type(a) != float) or type(b) != float:
        print("Valor inserido incorreto")
    else:
        s = a+b
        if s > 20.0:
            s = s + 8.0
        else:
            s = s - 5.0
    return s

a = float(input("Digite o valor do primeiro numero: "))
b = float(input("Digite o valor do segundo numero: "))
print(f"Resultado: {adicao(a,b)}")

def calcIMC(p,a: float):
    if type(p) != float or type(a) != float:
        print("os Valores inseridos estão incorretos, tente novamente.")
    else:
        return p/(a**2)

def comparaIMC(imc: float):
    if (imc < 17.0):
        print(f"Sua situacao eh: Muito abaixo do peso, IMC = {imc}")
    elif (17.0 <= imc < 18.5):
        print(f"Sua situacao eh: Abaixo do peso, IMC = {imc}")
    elif (18.5 <= imc <25.0):
        print(f"Sua situacao eh: Peso normal, IMC = {imc}")
    elif (25.0 <= imc < 30.0):
        print(f"Sua situacao eh: Acima do peso, IMC = {imc}")
    elif (30.0 <= imc < 35.0):
        print(f"Sua situacao eh: Obesidade I, IMC = {imc}")
    elif (35.0 <= imc < 40.0):
        print(f"Sua situacao eh: Obesidade II (severa), IMC = {imc}")
    elif (imc > 40.0):
        print(f"Sua situacao eh Obesidade III (mórbida), IMC = {imc}")

a = float(input("Digite a sua altura: "))
p = float(input("Digite o seu peso: "))
imc = calcIMC(p,a)
comparaIMC(imc)

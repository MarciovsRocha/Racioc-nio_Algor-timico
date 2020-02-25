while True:
    # faca um algoritimo que receba o valor do raio de uma circunferencia
    # e que retorne o valor do perimetro, diametro e area
    # ================================================================================================================
    # definindo os valores das constantes/variaveis
    r = 0
    pi = 3.1415
    escolha = 0 
    # funcao para calcular o perimetro da circunferencia 
    def calculaPerimetro(r, pi: float):
        P = (2 * pi * r)
        return P

    # funcao para calcular a area da circunferencia
    def calculaArea(r, pi: float):
        A = (pi * (r**2))
        return A

    # funcao para calcular o diametro da circunferencia
    def calculaDiametro(r: float):
        D = r * 2
        return D

    print("1 - Calcular Area")
    print("2 - Calcular Diametro")
    print("3 - Calcular Perimetro")
    escolha = float(input("escolha uma opcao: "))
    if ((escolha > 3) or (escolha < 1)):
        print("Voce entrou com uma opcao invalida")
    else:
        # variavel para receber o valor do raio da circunferencia
        r = float(input("Digite o valor do raio da circunferencia: "))
        if r <= 0 :
            print(f"O valor inserido eh invalido, favor verificar: {r}")
        elif escolha == 1:
            s = calculaArea(r, pi)
            print(f"o valor da ara da circunferencia eh: {s}")
        elif escolha == 2:
            di = calculaDiametro(r)
            print(f"o valor do diametro da circunferencia eh: {di}")
        elif escolha == 3:
            per = calculaPerimetro(r, pi)
            print(f"o valor do perimetro da circunferencia eh: {per}")
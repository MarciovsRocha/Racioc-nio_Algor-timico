def Cmenu():
    print('. : Banco G.M. : .')
    print('1- Saque')
    print('2- Depósito')
    print('3- Visualizar Saldo')
    print('4- Simular Investimento')
    choice = int(input('Opcao dejesada: '))
    return choice

# funcao para simulacoa de investimento
# onde F = valor do montante futuro ]
# | P valor inicial(aporte) 
# | n = numero de meses 
# | i = taxa de juros
def simulaInvestimento(P,n):
    i = 0.015 # rendimento de 1,5% ao mes
# taxa de administracao = 1$ a.a.
    if (n < 60):
        txAdm = 0.01
        totTX = ((n//12)*txAdm)
        F = P*(1+i)**n
        return (F-(F*totTX))
    if (n >= 60):
        txAdm = 0.005
        totTX = ((n//12)*txAdm)
        return (F-(F*totTX))
#calculo do montante: F = P*(1+i)**n


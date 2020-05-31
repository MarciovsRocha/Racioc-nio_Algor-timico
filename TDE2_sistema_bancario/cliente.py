import json

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

def visualizarSaldo(userLoged):
    if (userLoged == None):
        return 0
    print('. : Banco G.M. : . \n')
    print(f'Conta Corrente: {userLoged["id"]} \n Nome: {userLoged["nome"]} {userLoged["sobrenome"]} \n Saldo: {userLoged["balance"]}')
    input("\n Aperte [Enter] para continuar")

# funcao para realziar deposito na conta
def deposito(valor,conta):
    with open('./data/data.json') as json_file:
        data = json.load(json_file)
    lim = len(data['conta']) 
    for i in range(0,lim):
        if (data['conta'][i]['id'] == conta):
            saldoAntigo = data['conta'][i]['balance']
            saldoNovo = saldoAntigo + valor
            data['conta'][i]['balance'] = saldoNovo
    newData = data
    with open('./data/data.json', 'w') as outfile:
        json.dump(newData,outfile)
    return 1

def saque(valor,conta):
    with open('./data/data.json') as json_file:
        data = json.load(json_file)
    lim = len(data['conta']) 
    for i in range(0,lim):
        if (data['conta'][i]['id'] == conta):
            saldoAntigo = data['conta'][i]['balance']
            saldoNovo = saldoAntigo - valor
            data['conta'][i]['balance'] = saldoNovo
    newData = data
    with open('./data/data.json', 'w') as outfile:
        json.dump(newData,outfile)
    return 1
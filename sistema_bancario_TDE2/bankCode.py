import json
import sys
import os
verificado = False

# usuario logado
userLoged = {}

# id da conta, esta eh a PRIMARY KEY da conta, utilizada para realizar loging
# password eh a senha utilziada para fazer autenticacao do login
# nome do cliente, 
# saldo da conta do cliente
# tipo de conta C para Clientes G para Gerentes, utilizado para verificacao na hora de mostrar o menu

clear = lambda: os.system('cls')

# funcao para ler dados do arquivo JSON
def loadJSONData():
    with open('./data/data.json') as json_file:
        data = json.load(json_file)
        return data

# funcao para fazer login
def login(verificado, user, password, data):
    if (verificado == True):
        return 0
    lim = len(data['conta'])
    for i in range(0,lim):
        if ((user == data['conta'][i]['id']) and (password == data['conta'][i]['password'])):
            verificado = True
            print(data['conta'][i])
            print(verificado)
            return data['conta'][i]

def selectMenu(loggedUser):
    if ((loggedUser['type'] == 'G') or (loggedUser['type'] == 'g')):
        from gerente import menu as Gmenu
        Gmenu()
    elif ((loggedUser['type'] == 'C') or (loggedUser['type'] == 'c')):
        from cliente import menu as Cmenu
        Cmenu()

# funcao para salvar o arquivo json
def salvaData(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

# funcao para que o usuario faca login
def forcaLogin(verificado):
    # variavel para contar numero de tentavas e se estourar 
    # o limite cancela a execucao do programa para impedir 
    # que seja utilizado bruteforce para login
    contErros = 0 
    while (verificado != True):
        clear()
        user = int(input('Digite seu numero de conta: '))
        password = input('Digite sua senha: ')
        data = loadJSONData()
        userLoged = login(verificado,user,password,data)
        if (userLoged == None):
            print('Numero de conta ou senha invalido, tente novamente')
            v = input('Tentar novamente [S]im [N]ao')
            contErros += 1
            if ((v == 'N') or (v == 'n')):
                sys.exit(0)
            if (contErros == 3):
                print('Limite de tentativas expirado, tente novamente mais tarde!')
                sys.exit(0)
        else:
            verificado = True
            return userLoged, verificado

while True:
    if (verificado == True):
        clear()
        selectMenu(userLoged)
    else:
        print('Deseja fazer login? [S]im [N]ao')
        v = input()
        if ((v == 'S') or (v == 's')):
            userLoged, verificado = forcaLogin(verificado)
        elif ((v == 'N') or (v == 'n')):
            sys.exit(0)


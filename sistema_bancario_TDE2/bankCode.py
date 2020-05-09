import json
import sys
import os
from gerente import *
from cliente import *
verificado = False

# usuario logado
userLoged = {}

# id da conta, esta eh a PRIMARY KEY da conta, utilizada para realizar loging
# password eh a senha utilziada para fazer autenticacao do login
# nome do cliente, 
# saldo da conta do cliente
# tipo de conta C para Clientes G para Gerentes, utilizado para verificacao na hora de mostrar o menu

clear = lambda: os.system('cls')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para ler dados do arquivo JSON
def loadJSONData():
    with open('./data/data.json') as json_file:
        data = json.load(json_file)
        return data

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para fazer login
def login(verificado, user, password, data):
    if (verificado == True):
        return 0
    lim = len(data['conta'])
    for i in range(0,lim):
        if ((user == data['conta'][i]['id']) and (password == data['conta'][i]['password'])):
            verificado = True
            return data['conta'][i]

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def geraIDNovo(data):
    pos = len(data['conta'])
    ultimoId = data['conta'][pos-1]['id']
    idNovo = ultimoId+1
    return idNovo

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def selectMenu(loggedUser):
    if ((loggedUser['type'] == 'G') or (loggedUser['type'] == 'g')):
        escolha = Gmenu()
        if (escolha == 1):
            data = loadJSONData()
            idNovaConta = (geraIDNovo(data))
            newuser = cadUser(idNovaConta)
            salva = input('Deseja Salvar as alteracoes feitas? [S]im [N]ao\n')
            if ((salva == 's') or (salva == 'S')):
                salvaData(newuser)
        elif (escolha == 2):
            srcNome = input('Digite o Nome a ser buscado:\n')
            data = loadJSONData()
            result = buscaConta(srcNome,data)
            print(f'Resultado para a busca: {srcNome}')
            for i in range(len(result)):
                print(f'id: {result[i]["id"]} -- nome: {result[i]["nome"]} {result[i]["sobrenome"]}\n ')
        elif(escolha == 3):
            idConta = int(input('Digite o ID da Conta cuja senha sera troca: '))
            senhaNova = input('Digite a senha para o cliente de 4 a 8 digitos \n caracteres aceitos: a-z, A-Z,0-9 \n Senha:')
            data = loadJSONData()
            newData = trocaSenhaConta(idConta,senhaNova,data)
            # criar procedimento para alterar a data
            with open('./data/data.json', 'w') as outfile:
                json.dump(newData,outfile)
    elif ((loggedUser['type'] == 'C') or (loggedUser['type'] == 'c')):
        escolha = Cmenu()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para salvar o arquivo json
def salvaData(object):
    jsonFile = json.loads(open('./data/data.json').read())
    jsonFile['conta'].append(object)
    with open('./data/data.json', 'w') as outfile:
        outfile.write(json.dumps(jsonFile))
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
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
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
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


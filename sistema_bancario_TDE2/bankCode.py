# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# import section
import json # biblioteca para trabalhar com formato JSON
import sys # verificar se a biblioteca esta sendo utilizada
from os import system as osSys # bilbioteca utilizada para criar o metodo clear
from gerente import * # importa as funcoes do arquivo gerente.py
from cliente import * # importa as funcoes do arquivo cliente.py
from time import sleep # importa a funcao sleep da biblioteca time
# /import section
# ------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# var section
# variavel global para controle de login
verificado = False # por padrao ela inicia como False pois ngm fez login ainda

# variavel global para receber as informalcoes do usuario logado
userLoged = {} 
# /var section
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# metodo para limpar o console
clear = lambda: osSys('cls') # para limpar o console basta chamar clear()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para ler dados do arquivo JSON
# abre o arquivo data.json da pasta data e grava na variavel data que eh passada para o return
# so chame esta funcao se vc quiser todos os dados
def loadJSONData():
    with open('./data/data.json') as json_file:
        data = json.load(json_file)
        return data

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para fazer login
# esta funcao eh chamada sempre que verificado == False
def login(verificado, user, password, data):
    # verifica se a funcao nao foi chamada por engano, caso verificado seja true a funcao retorna 0 como 'default'
    if (verificado == True):
        return 0
    lim = len(data['conta'])
    for i in range(0,lim):
        if ((user == data['conta'][i]['id']) and (password == data['conta'][i]['password'])):
            verificado = True
            return data['conta'][i] # assim que autenticado o login retona as informacoes do usuario logado para ser gravada na variavel userLoged

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para gerar um novo ID
# utiliza as informacoes da variavel data para verificar qual eh o ultimo 
# id cadastrado e adiciona +1 para gerar um novo ID e retorna o novo ID
def geraIDNovo(data):
    pos = len(data['conta'])
    ultimoId = data['conta'][pos-1]['id']
    idNovo = ultimoId+1
    return idNovo

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para mostrar o menu de opcoes
# ela se baseia no type do usuario para chamar a funcao de exibir opcoes
def selectMenu(loggedUser):
# type 'G' == gerente
# type 'C' == cliente
    # verifica se a conta tem type 'G' 
    if ((loggedUser['type'] == 'G') or (loggedUser['type'] == 'g')):
        escolha = Gmenu() # chama a funcao para mostrar o menu do gerente
        if (escolha == 1): # se a escolha for 1 prepara os parametros e chama as funcoes necessarias
            data = loadJSONData() # carrega as informacoes e grava na variavel data
            idNovaConta = (geraIDNovo(data)) # variavel que recebe o novo ID
            # cadUser esta no arquivo gerente.py pois eh uma fincao executada somente por um gerente
            newuser = cadUser(idNovaConta)
            salva = input('Deseja Salvar as alteracoes feitas? [S]im [N]ao\n') # verifica se o gerente quer salvar as alteracoes
            if ((salva == 's') or (salva == 'S')):
                salvaData(newuser) # chama a funcao para adicionar o novo cliente no final do documento
                clear() # limpa o console
                print('Novo Usuario Salvo com Sucesso!')
                sleep(1) # espera 1 segundo antes de continuar
            elif ((salva == 'N') or (salva == 'n')): # verifica se a opcao escolhida foi de nao salvar alteracoes
                print('Alteracoes descartadas.')
                sleep(1) # espera 1 segundo antes de continuar
        elif (escolha == 2): # se a escolha for 2 prepara os parametros e chama as funcoes necessarias
            srcNome = input('Digite o Nome a ser buscado:\n')
            data = loadJSONData() # chama a funcao para gravar o conteudo do arquivo data.json na variavel data
            # buscaConta() esta no arquivo gerente.py pois eh uma funcao executada somente por um gerente
            result = buscaConta(srcNome,data) # passa como parametro o conteudo do arquivo data.json na pasta data para pesquisa
            print(f'Resultado para a busca: {srcNome}')
            for i in range(len(result)): # metodo para listar os ID's e nomes recebidos como resultado 
                print(f'id: {result[i]["id"]} -- nome: {result[i]["nome"]} {result[i]["sobrenome"]}\n ')
        elif(escolha == 3): # se a escolha for 2 prepara os parametros e chama as funcoes necessarias
            idConta = int(input('Digite o ID da Conta cuja senha sera troca: ')) # id da conta a ser trocada a senha
            senhaNova = input('Digite a senha para o cliente de 4 a 8 digitos \n caracteres aceitos: a-z, A-Z,0-9 \n Senha:') # nova senha
            data = loadJSONData() # chama a funcao para gravar o conteudo do arquivo data.json na variavel data
            # trocaSenhaConta esta no arquivo gerente.py pois eh uma funcao executada somente por um gerente 
            newData = trocaSenhaConta(idConta,senhaNova,data) # pega o resultado e salva no arquivo JSON
            # criar procedimento para alterar a data
            with open('./data/data.json', 'w') as outfile:
                json.dump(newData,outfile)
    elif ((loggedUser['type'] == 'C') or (loggedUser['type'] == 'c')):
        escolha = Cmenu()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# funcao para adicionar um novo objeto 'conta' ao final do arquivo data.json
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
        userLoged = {} # assim que identificado que o usuario nao esta logado ele apaga as informacoes da variavel userLoged
        print('Deseja fazer login? [S]im [N]ao')
        v = input()
        if ((v == 'S') or (v == 's')):
            userLoged, verificado = forcaLogin(verificado)
        elif ((v == 'N') or (v == 'n')):
            sys.exit(0)


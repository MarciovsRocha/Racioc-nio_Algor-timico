def Gmenu():
    print('. : Banco G.M. : .')
    print('1- Cadastrar nova conta')
    print('2- Busca de Conta Corrente')
    print('3- Definicao de Nova senha')
    choice = int(input('Opcao dejesada: '))
    return choice

def cadUser(id):
    nomeCliente = input('Digite o Nome do cliente:\n')
    sobreNome =input('Digite o sobrenome do cliente \n')
    profissao = input('Digite a Profissao do cliente\n')
    rendaMensal = float(input('Digite a renda mensal do cliente: (formato: ###.#)\n'))
    endereco = input('Digite o endereco do cliente:\n')
    telefone = input('Digite o telefone de contato do cliente:\n')
    senha = input('Digite a senha para o cliente de 4 a 8 digitos \n caracteres aceitos: a-z, A-Z,0-9 \n Senha:')
    # colocar uma funcao para verificar a senha antes dele criar o objeto cliente
    newUser = {"id": id,"password": senha,"nome": nomeCliente, "sobrenome": sobreNome, "balance": 0.0,"type": "c", "endereco":  endereco, "telefone": telefone, "profissao": profissao, "rendaMensal": rendaMensal}
    return newUser

def buscaConta(nome, data):
    len_clientes = len(data['conta'])
    listaContas = []
    for i in range(0,len_clientes):
        if (nome == data['conta'][i]['nome']):
            listaContas.append(data['conta'][i])
    return listaContas

def trocaSenhaConta(id, senhaNova, data):
    for i in range(0,len(data['conta'])):
        if (id == data['conta'][i]["id"]):
            data['conta'][i]['password'] = senhaNova
            return data
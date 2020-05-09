def Gmenu():
    print('. : Banco G.M. : .')
    print('1- Cadastrar nova conta')
    print('2- Busca de Conta Corrente')
    print('3- Definicao de Nova senha')
    choice = int(input('Opcao dejesada: '))
    return choice

def cadUser(id):
    nomeCliente = input('Digite o Nome completo do cliente:\n')
    profissao = input('Digite a Profissao do cliente\n')
    rendaMensal = float(input('Digite a renda mensal do cliente: (formato: ###.#)\n'))
    endereco = input('Digite o endereco do cliente:\n')
    telefone = input('Digite o telefone de contato do cliente:\n')
    senha = input('Digite a senha para o cliente de 4 a 8 digitos \n caracteres aceitos: a-z, A-Z,0-9 \n Senha:')
    newUser = {"id": id,"password": senha,"nome": nomeCliente, "balance": 0.0,"type": "c", "endereco":  endereco, "telefone": telefone, "profissao": profissao, "rendaMensal": rendaMensal}
    return newUser
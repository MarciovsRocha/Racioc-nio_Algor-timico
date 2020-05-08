import json
import unicodedata
import re
#-------------------------*----------------------------------
#- Definição de nova senha: O sistema requisitará o número de uma conta
#corrente e verificará se a conta existe. Se a conta existir, o sistema
#requisitará uma nova senha, que deverá possuir entre 4 a 8 caracteres
#alfanuméricos. O sistema deverá recusar senhas com acentos e/ou caracteres
#especiais
try:
    nomegerent=open('nomegerente','rb')
    nomeGerent=nomegerent.readline()
    nomeGerent=nomeGerent.decode()
    nomeGerent=json.loads(nomeGerent)
    nomegerent.close()
except:
    nomedogerente=open("nomegerente","wb")
    nomeGerent=input("Digite seu nome por favor: ")
    nomedogerente_js=json.dumps(nomeGerent)
    nomedogerente.write(nomedogerente_js.encode())
    nomedogerente.close()
try:
    matrizdepessoas=open('matrizdepessoas','rb')
    matriz=matrizdepessoas.readline()
    matriz=matriz.decode()
    matriz=json.loads(matriz)
    linha=len(matriz)
    matrizdepessoas.close()
except:
    matriz=[]
    linha=len(matriz)
def salva_e_carrega_matriz(matriz):
    #salvando------------------------------------------------------
    salva=open('matrizdepessoas','wb')
    salva_js=json.dumps(matriz)
    salva.write(salva_js.encode())
    salva.close()
    #carregando==============================
    matrizdepessoas=open('matrizdepessoas','rb')
    matriz=matrizdepessoas.readline()
    matriz=matriz.decode()
    matriz=json.loads(matriz)
    linha=len(matriz)
    matrizdepessoas.close()
    

#---------------------------------------------------------------------------NOME DO GERENTE
def criando_espaço(matriz):
    cont=1
    adiciona=1
    while adiciona<=1:
        matriz.append([])
        while cont<=8:
            matriz[linha].append(0)
            cont+=1
        adiciona+=1
        cont=1
        adicionandoconta(matriz)
        
def adicionandoconta(matriz):
    for i in range(0,7):
        if i==0:
            tok=True
            ok=True
            valor=0
            while ok:
                matriz[linha][i]=input("Digite o numero da conta, tendo 5 caracter numericos: ")
                if matriz[linha][i].isnumeric() and len(str(matriz[linha][i]))==5:
                    valor=int(matriz[linha][i])
                    ok=False
                else:
                    if not ok:
                        break
        elif i ==1:
            matriz[linha][i]= input("Digite o nome: ")
            matriz[linha][i]=matriz[linha][i].split()
        elif i ==2:
            matriz[linha][i]=input("Digite seu endereço: ")
        elif i ==3:
            matriz[linha][i]=input("Digite a sua profissão: ")
        elif i ==4:
            matriz[linha][i]=input("Digite o seu telefone: ")
        elif i==5:
            ook=True
            value=0
            while ook:
                matriz[linha][i]=input("Digite sua renda mensal: ")
                if matriz[linha][i].isnumeric():
                    value= int(matriz[linha][i])
                    ook=False
                else:
                    if not ook:
                        break
        elif i==6:
            matriz[linha][i]=input("Digite sua senha: ")
            matriz[linha][i]=removerAcentosECaracteresEspeciais(matriz[linha][i])
        salva=open('matrizdepessoas','wb')
        salva_js=json.dumps(matriz)
        salva.write(salva_js.encode())
        salva.close()
    voufazer(matriz)                                   


def buscandoconta(matriz):
    caça=input("que nome procura: ").split()
    for i in range(0,len(matriz),1):
        for a in range(0,len(caça),1):
            if matriz[i][1][a]==caça[a]:
                print(matriz[i])
                i+=i

            
    print('-------------------------------------------------------------------------------')
    voufazer(matriz)

def alterarsenha(matriz):
    n_cont_corrente=int(input("Favor, Digite o numero da conta que deseja alterar a senha: "))
    for i in range(0,len(matriz),1):
        if int(matriz[i][0])== n_cont_corrente:
            print('Conta encontrada!!!')
            print()
            matriz[i][6]=input("Digite a nova Senha: ")
            matriz[i][6]=removerAcentosECaracteresEspeciais(matriz[i][6])
        else:
            print("conta inexistente!.")
    salva_e_carrega_matriz(matriz)
    voufazer(matriz)
    
def removerAcentosECaracteresEspeciais(palavra):
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
   
def voufazer(matriz):
    justdoit=int(input(f"olá , senhor {nomeGerent}\n Digite 1 caso queira adicionar uma nova conta.\n Digite 2 caso queira buscar uma conta corrente.\n Digite 3 caso queira definir uma nova senha de uma conta."))
    while justdoit >=4 or justdoit<=0:
        input("comando invalido")
        justdoit=int(input(f"olá , senhor {nomeGerent}\n Digite 1 caso queira adicionar uma nova conta.\n Digite 2 caso queira buscar uma conta corrente.\n Digite 3 caso queira definir uma nova senha de uma conta."))    
    if justdoit==1:
        criando_espaço(matriz)
    elif justdoit==2:
        buscandoconta(matriz)
    elif justdoit==3:
        alterarsenha(matriz)
voufazer(matriz)

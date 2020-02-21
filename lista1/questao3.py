# exercicio 3 da lista 1 
# Faca um programa que receba um valor que eh o valor pago, 
# um segundo valor que eh o preco do produto e retorne o troco a ser dado
#============================================================================================================
# funcao para realizar o cálculo de troco
def calculaTroco(x, y):
    return x-y

valProd = float(input("Insira o valor do produto:   R$")) # variável que recebe o valor do[s] produto[s]
valPago = float(input("Insira o valor pago:         R$")) # variável que recebe o valor do pago pelo cliente

# condicional para verificar se o valor pago é maior 
if (valPago < valProd):
    print("O valor pago eh inferior ao valor do produto!")
    print("verifique novamente se os valores estao corretos")
else:  # se os valores estiverem corretos chama a funcao para realizar o calculo e armazenar na variavel troco
    troco = calculaTroco(valPago, valProd)
    print(f"O troco a ser dado eh:  R${troco}")
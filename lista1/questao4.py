# questão 4
# faca um progama que receba o valor do quilo de um produto 
# =========================================================================================================
# funcao para calular o valor do produto
def calculaPreco(x,y):
    return x*y

pesoQuilo = float(input("Insira o peso do produto em quilos:  ")) # variavel que recebe o peso em quilos do produto
valorQuilo = float(input("Insira o valor do Quilo do produto: R$")) # variavel que recebe o valor do quilo do produto

if (valorQuilo < 0) or (pesoQuilo < 0):
    print("Valores incompatíveis!")
    print("Voce deve ter inserido algum valor negativo, favor verificar os valores inseridos e corrigi-los")
    print(f"Peso Inserido: {pesoQuilo}")
    print(f"Valor do Quilo: {valorQuilo}")
else: 
    preco = calculaPreco(pesoQuilo,valorQuilo)
    print(f"Preco a ser pago: {preco}")
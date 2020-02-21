# recebendo informacao do usuario do numero de aulas
qtdAulas = float(input("Quantidade de aulas:  "))
# recebendo a porcentagem permitida de faltas do usuario
numeroPerc = input("Insira a porcentagem de faltas permitidas:  ")
# convertendo a porcentagem inserida para float em string
percFaltas = "0." + numeroPerc
# calculando a qtde de aulas permitidas a partir dos inputs
faltasPossiveis = float(qtdAulas * float(percFaltas))  
print(f"A quantidade de faltas possiveis eh {faltasPossiveis}")
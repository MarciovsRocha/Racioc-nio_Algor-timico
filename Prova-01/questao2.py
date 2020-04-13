# Um programador foi incumbido de escrever uma rotina em Python
# que lesse um valor usando o comando input e verificasse se ele
# é par ou não. Caso o número informado seja par, ele deve ser
# acrescido de 10 e então apresentado na tela.
# Caso o número seja ímpar, deve-se verificar também se ele é
# múltiplo de 3 ou de 7. Caso seja, ele deve ser multiplicado por
# 70 e então apresentado na tela. Caso o número não se enquadre em
# nenhuma destas condições, o próprio número deve ser informado.

n = input('numero: ')
if (n % 2 == 0):
    print(n+10)
elif (n % 3 == 0) or (n % 7 == 0):
    print(n * 70)
else:
    print(n)

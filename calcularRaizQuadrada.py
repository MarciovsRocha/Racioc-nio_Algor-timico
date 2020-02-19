# recebendo informacao do usuario
numero = float(input("Digite um Numero:  "))
# verificacao se o usuario quer calcular a radiciacao deste numero
if (input("Deseja Calcular a raiz quadrada [s]im"  ) == 's'):
  radiciacao = (numero**1/2) # ao multiplicar um numero pelo inverso do expoente obtem o resultado de radiciacao
  print(f"o Raiz quadrada de {numero}") 
# recebendo informacao do usuario
numero = float(input("Digite um Numero:  "))
# verificacao se o usuario quer verificar o sucessor deste numero
if (input("Deseja Calcular o sucessor [s]im"  ) == 's'):
  sucessor = float(numero + 1)
  print(f"o sucessor de {numero} eh {sucessor}") # imprimindo o sucessor do numero
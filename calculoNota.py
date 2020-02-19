while True : 
  nota = [] # criando array de notas
  i = 1 #variavel contador
  
  # funcao para adicionar notas no array nota
  def adicionarNota():
    nota.append(float(input("Digite a nota:")))

  def calcularMedia():
    while i <= len(nota):
      soma = soma + nota[i]
      i++
      

  # condicional para verificar se o usuário quer adicionar outra nota
  if (input("Deseja adicionar mais notas [s]im [n]a:  ") == 's'):
    adicionarNota()

  if (input("Deseja calcular a media [s]im [n]ao:  ") == 's'):
    calcularMedia()
def verifica(n: int):
    if (n % 3 == 0) and (n % 7 == 0): # condicional para verificar se o numero eh divisivel por 3 e por 7
        print(f"o numero {n} eh divisel por 3 e por 7.")
    elif (n % 3 == 0) and (n % 7 != 0): # condicional para verificar se o numero eh divisivel somente por 3
        print(f"o numero {n} eh divisivel somente por 3")
    elif (n % 3 != 0) and (n % 7 == 0): # condicional para verificar se o numero eh divisiel somente por 7
        print(f"o numero {n} eh divisivel somente por 7")
    else: # saida padrao caso o numero nao seja divisivel 
        print(f"o numero {n} nao eh divisivel por 3 nem por 7")

n = int(input("Digite um numero inteiro: "))
verifica(n)
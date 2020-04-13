def verifica(n: ﻿int):
    if (n % 5 == 0) and (n % 12 == 0):
        print(f"o numero {n} eh divisel por 5 e por 12.")
    elif (n % 5 == 0) and (n % 12 != 0): # condicional para verificar se o numero eh divisivel somente por 5
        print(f"o numero {n} eh divisivel somente por 5")
    elif (n % 5 != 0) and (n % 12 == 0): # condicional para verificar se o numero eh divisiel somente por 12
        print(f"o numero {n} eh divisivel somente por 12")﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
    else: # saida padrao caso o numero nao seja divisivel 
        print(f"o numero {n} nao eh divisivel por 5 nem por 12")

n = int(input("Digite um numero inteiro: "))
verifica(n)

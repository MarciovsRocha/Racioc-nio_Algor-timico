Lista =[]
def ComparaNumero (A,B,C: int):
    if (A<B):
        if (B<C) and (A<C):
            Lista.append(A)
            Lista.append(B)
            Lista.append(C)
        else:
            Lista.append(A)
            Lista.append(C)
            Lista.append(B)
    elif (B<C):
        if(C<A)and(B<A):
            Lista.append(B)
            Lista.append(C)
            Lista.append(A)
        else:
            Lista.append(B)
            Lista.append(A)
            Lista.append(C)
    else:
        if(C<B)and(B<A):
            Lista.append(C)
            Lista.append(B)
            Lista.append(A)
        else:
            Lista.append(C)
            Lista.append(A)
            Lista.append(B)


A=int(input("Digite o Primeiro Digito: "))
B=int(input("Digite o Segundo Digito: "))
C=int(input("Digite o Terceiro Digito: "))

ComparaNumero(A,B,C)
print(Lista)

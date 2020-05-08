# funcoes recursivas
# n! = { 1, se n = 1 ou n = 0 | n*(n-1)! }
#
def fat_recursivo(n):
	# caso de erro (criterio de parada)
    if n < 0:  
        return -1
    # criterio de parada
    elif n == 0 or n == 1: # se o valor de {(0!) && (1!)} == 1 
        return 1
    else:
        return n * fat_recursivo(n-1)



#def verificaMaiorVetor(X): # X == vetor
#    if (n == len(X-1)):
        
    



#print(fat_recursivo(4))

#sequencia = {1,3,4,0,7}
#verificaMaiorVetor(0,sequencia)


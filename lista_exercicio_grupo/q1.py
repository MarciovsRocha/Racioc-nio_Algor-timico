def termoPA(r,a1,n: float):
    return a1 + r*(n-1)

r = float(input("Insira a Razão da PA: "))
a1 = float(input("Insira o primeiro termo da PA: "))
n = float(input("Insira o qual termo deseja descobrir da PA: "))
result = termoPA(r,a1,n)
print(f"O valor do termo {n} eh: {result}")
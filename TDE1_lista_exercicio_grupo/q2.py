import math
def calcAreaTriangulo(a,b,c: float):
    if a <=0 or b <=0 or c <=0:
        print("Valor inserido incorreto")
    else:
        p = (a+b+c)/2
        return math.sqrt((p*(p-a)*(p-b)*(p-c)))

print(calcAreaTriangulo(5.5,7.6,3.8))
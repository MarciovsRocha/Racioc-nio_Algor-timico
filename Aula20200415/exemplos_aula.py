import math
# ===============================================================================================================
def delta(a,b,c: float):
    d = ( (b*b) - (4 * a * c) )
    if (d <= 0):
        return False
    return  d

def bhaskara(a, b, c: float):
    x = []
    if (delta(a,b,c)):
        return 0
    x1 = ( ((-b) - (delta(a,b,c) ** 0.5) ) / (2*a) )
    x2 = ( ((-b) + (delta(a,b,c) ** 0.5) ) / (2*a) )
    if (x1 == x2):
        return x1
    x.append(x1)
    x.append(x2)
    return x 

result = bhaskara(1.0,16.0,8.0)
if (type(result) == "list"):
    print(f"X': {result[0]} \n")
    print(f"X'': {result[1]} \n")
else:
    print(f"X: {result}")
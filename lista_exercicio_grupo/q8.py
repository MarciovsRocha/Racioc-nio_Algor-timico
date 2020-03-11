idade = 22
peso = 58

# 500mg por ml
# 1ml = 20gotas
# 20gotas = 500mg
# 1gota = 25mg

if idade >= 12:
    if peso >= 60: dose = 1000
    else: dose = 875
else:
    if peso > 30: dose = 750
    elif peso > 24.1: dose = 500
    elif peso > 16.1: dose = 375
    elif peso > 9.1: dose = 250
    elif peso > 5: dose = 500
    else: dose = 0

gotas = int(dose/25)

print("Paciente deve tomar " + str(gotas) + " gotas")
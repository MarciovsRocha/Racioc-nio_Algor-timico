peso = float(input('peso:'))
altura = float(input('altura:'))
imc = (peso / (altura ** 2))
print(imc)
if imc < 17:
    print('Muito abaixo')
elif imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print ('Normal')
elif imc < 30:
    print('Acima')
elif imc < 35:
    print('obesidade 1')
elif imc < 40:
    print('obesidade 2')
elif imc >= 40:
    print('obesidade 3')

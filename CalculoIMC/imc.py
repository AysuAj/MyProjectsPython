print('---'*20)
print(f'{"CÁLCULO IMC":^60}')
print()
nome = str(input('Informe o seu nome: '))
altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))
print()
print()

print('--'*20)
print(f'{"DADOS INFORMADOS":^40}')
print(f'Nome: {nome}')
print(f'Altura: {altura}')
print(f'Peso: {peso}')
print()
print()

print('--'* 20)
print(f'{"DIAGNÓSTICO":^40}')
print()

imc = peso / (altura*altura)

if imc < 17:
    print(f'IMC: {imc:.2f} - Situação: Muito abaixo do peso')
elif imc >= 17 and imc < 18.50:
    print(f'IMC: {imc:.2f} - Situação: Abaixo do peso')
elif imc >= 18.50 and imc < 25:
    print(f'IMC: {imc:.2f} - Situação: Peso normal')
elif imc >= 25 and imc < 30:
    print(f'IMC: {imc:.2f} - Situação: Acima do peso')
elif imc >= 30 and imc < 35:
    print(f'IMC: {imc:.2f} - Situação: Obesidade I')
elif imc >= 35 and imc < 40:
    print(f'IMC: {imc:.2f} - Situação: Obesidade II(severa)')
else:
    print(f'IMC: {imc:.2f} - Situação: Obesidade III(mórbida)')

print('--'*20)



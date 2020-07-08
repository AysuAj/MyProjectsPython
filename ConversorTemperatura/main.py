import calculos

calc = calculos.Calculos()

print()
print('--' * 30)
print(f'{"CONVERSOR DE TEMPERATURA":^60}')
print('--' * 30)
print()
calc.number = float(input("Digite a temperatura: "))
print()
print()
print('--' * 30)
print(f'{"OPÇÕES":^60}')
print()
print('     1- Celsius para Fahrenheit')
print('     2- Celsius para Kelvin')
print('     3- Fahrenheit para Celsius')
print('     4- Fahrenheit para Kelvin')
print('     5- Kelvin para Celsius')
print('     6- Kelvin para Fahrenheit')
print()
choose = int(input('::  '))
print()
if choose == 1:
    print(calc.celsiusToFahrenheit())
if choose == 2:
    print(calc.celsiusToKelvin())
if choose == 3:
    print(calc.fahrenheitToCelsius())
if choose == 4:
    print(calc.fahrenheitToKelvin())
if choose == 5:
    print(calc.kelvinToCelsius())
if choose == 6:
    print(calc.kelvinToFahrenheit())

print()
print()

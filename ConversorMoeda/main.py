import scraping

convMoeda = scraping.WebScraping()

print()
print('--' * 30)
print(f'{"CONVERSOR DE MOEDA":^60}')
print()
convMoeda.number = float(input("Informe o valor: "))
print()
print('--' * 30)
print(f'{"Opções":^60}')
print()
print('     1- Real para Dólar')
print('     2- Dólar para Real')
print('     3- Real para Euro')
print('     4- Euro para Real')
entrada = int(input(":: "))
if entrada == 1:
    print(f'R${convMoeda.number}')
    print(f'${convMoeda.realToDolar()}')
if entrada == 2:
    print(f'${convMoeda.number}')
    print(f'R${convMoeda.dolarToReal()}')
if entrada == 3:
    print(f'R${convMoeda.number}')
    print(convMoeda.realToEuro())
if entrada == 4:
    print(f'R${convMoeda.number}')
    print(convMoeda.euroToReal())

print()
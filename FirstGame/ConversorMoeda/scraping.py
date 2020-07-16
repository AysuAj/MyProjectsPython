import requests
from bs4 import BeautifulSoup

class WebScraping:
    def __init__(self):
        self.number = 0
        self.realDolarScraping()
        self.realEuroScraping()
    
    def realDolarScraping(self):
        page = requests.get('https://economia.uol.com.br/cotacoes/')
        soup = BeautifulSoup(page.content, 'html.parser')
        textFind = soup.find_all('a', class_="subtituloGrafico subtituloGraficoValor")
        textDiv = textFind[0].text
        textRep = textDiv.replace(',', '.')
        textFT = textRep[3:]
        textFloat = float(textFT)
        self.realDolarBase = textFloat
    
    def realEuroScraping(self):
        page = requests.get('https://economia.uol.com.br/cotacoes/')
        soup = BeautifulSoup(page.content, 'html.parser')
        textFind = soup.find_all('a', class_="subtituloGrafico subtituloGraficoValor")
        textDiv = textFind[-1].text
        textRep = textDiv.replace(',', '.')
        textFT = textRep[3:]
        textFloat = float(textFT)
        self.realEuroBase = textFloat
    
    def realToDolar(self):
        realDolar = self.number / self.realDolarBase
        return round(realDolar, 2)
    
    def dolarToReal(self):
        dolarReal = self.number * self.realDolarBase
        return round(dolarReal, 2)

    def realToEuro(self):
        realEuro = self.number / self.realEuroBase
        return round(realEuro, 2)

    def euroToReal(self):
        euroReal = self.number * self.realEuroBase
        return round(euroReal, 2)
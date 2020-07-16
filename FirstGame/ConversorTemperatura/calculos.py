class Calculos:
    def __init__(self):
        self.number = 0

    def celsiusToFahrenheit(self) -> float:
        celFah = (self.number * 9 / 5) + 32
        return round(celFah, 1)

    def celsiusToKelvin(self):
        celKel = self.number + 273.15
        return round(celKel, 1)

    def fahrenheitToCelsius(self):
        fahCel = (self.number - 32) * 5 / 9
        return round(fahCel, 1)

    def fahrenheitToKelvin(self):
        fahKel = (self.number - 32) * 5 / 9 + 273.15
        return round(fahKel, 1)

    def kelvinToCelsius(self):
        kelCel = self.number - 273.15
        return round(kelCel, 1)

    def kelvinToFahrenheit(self):
        kelFah = (self.number - 273.15) * 9 / 5 + 32
        return round(kelFah, 1)
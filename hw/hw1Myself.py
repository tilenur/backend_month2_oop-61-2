class Country:
    def __init__(self, name, region, capital, population):
        self.name = name
        self.region = region
        self.capital = capital
        self.population = population

    def info(self):
        return f"{self.name} is in {self.region}, has capital ({self.capital}) and with the population of {self.population} people."

    def big_country(self):
        if self.population > 10:
            return  f"{self.name} has a big population (over 10 mill)"
        else:
            return f"{self.name} has a small population"

Japan = Country("Japan", "Asia", "Tokyo", 14)
Kyrgyzstan = Country("Kyrgyzstan", "Asia", "Bishkek", 2)

print(Japan.info())
print(Kyrgyzstan.info())

print(Japan.big_country())
print(Kyrgyzstan.big_country())
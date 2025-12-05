class Phone:

    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.is_on = False

    def turn_on(self):
        if self.battery > 0:
            self.is_on = True
            return f"{self.brand} {self.model} включён."
        else:
            return f"{self.brand} {self.model} не может включиться — батарея разряжена."

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        return f"Телефон заряжен. Текущий заряд: {self.battery}%"

    def info(self):
        status = "включён" if self.is_on else "выключен"
        return f"{self.brand} {self.model} — заряд {self.battery}%, статус: {status}"


phone1 = Phone("Apple", "iPhone 14", 25)
phone2 = Phone("Samsung", "Galaxy S23", 0)
phone3 = Phone("Xiaomi", "Mi 12", 80)

print(phone1.info())
print(phone1.turn_on())
print(phone1.charge(50))
print(phone1.info())

print("\n" + phone2.info())
print(phone2.turn_on())
print(phone2.charge(30))
print(phone2.turn_on())

print("\n" + phone3.info())
print(phone3.turn_on())
print(phone3.info())

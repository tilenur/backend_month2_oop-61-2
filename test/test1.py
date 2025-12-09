from abc import ABC, abstractmethod

# 1
class Hero:
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self) -> str:
        return f"{self.name} готов к бою!"


# 2
class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self) -> str:
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def action(self) -> str:
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


# 3
class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero: Hero, balance: int, password: str):
        self.hero = hero
        self._balance = balance
        self.__password = password

    # --- методы ---
    def login(self, password: str) -> bool:
        return password == self.__password

    @property
    def full_info(self) -> str:
        return f"Герой: {self.hero.name}, уровень: {self.hero.lvl}, баланс: {self._balance} SOM"

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    def bonus_for_level(self) -> int:
        return self.hero.lvl * 10

# 4
    def __str__(self) -> str:
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return "Ошибка: Нельзя сложить счета героев разных классов!"

        if type(self.hero) is type(other.hero):
            return self._balance + other._balance

        return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other) -> bool:
        if not isinstance(other, BankAccount):
            return False
        return (
            self.hero.name == other.hero.name
            and self.hero.lvl == other.hero.lvl
        )
# 5
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone: str):
        pass


class KGSms(SmsService):
    def send_otp(self, phone: str) -> str:
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone: str) -> dict:
        return {
            "text": "Код: 1234",
            "phone": phone,
        }

if __name__ == "__main__":
    mage1 = MageHero("Merlin", 80, 500, 150)
    mage2 = MageHero("Merlin", 80, 500, 200)
    warrior = WarriorHero("Conan", 50, 900, 20)

    acc1 = BankAccount(mage1, 5000, "1234")
    acc2 = BankAccount(mage2, 3000, "0000")
    acc3 = BankAccount(warrior, 2500, "1111")

    print(mage1.action())
    print(warrior.action())

    print(acc1)
    print(acc2)

    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    print("\nСумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)

    print("\nMage1 == Mage2 ?", acc1 == acc2)
    print("Mage1 == Warrior ?", acc1 == acc3)

    sms = KGSms()
    print("\n", sms.send_otp("+996777123456"))

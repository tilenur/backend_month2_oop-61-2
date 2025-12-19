from faker import Faker

# Faker — это внешняя библиотека, которая используется
# для генерации фейковых (тестовых) данных:
# имён, email-адресов, телефонов, адресов и т.д.

fake = Faker()

name = fake.name()
email = fake.email()
address = fake.address()

print("Name:", name)
print("Email:", email)
print("Address:", address)
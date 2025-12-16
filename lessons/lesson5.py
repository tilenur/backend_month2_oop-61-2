# Статический метод (@staticmethod)

# class Math:
#
#     def __init__(self, d, c):
#         self.d = d
#         self.c = c
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def subtract(j, i):
#         return j - i
# print(Math.add(12, 12))
# print(Math.subtract(12,1))


# 2. Метод класса (@classmethed)

# class User:
#     # Атрибуты класса / Class attributes
#     default_role = "guest"
#
#     def __init__(self, name, role: str = "n/a"):
#         # Атрибуты экземпляра класса / Class instance attributes
#         self.name = name
#         self.role = role
#
#     @classmethod
#     def create_from_name(cls, name):
#         return cls(name, cls.default_role)
#
#     @classmethod
#     def get_base_role(cls):
#         return cls.default_role
#
#     def get_name(self):
#         return self.name
#
# user_1 = User.create_from_name("User")
# ardager = User("Ardager", "admin")
#
# print(user_1.name)
# print(ardager.name)
#
#
# # ardager = User("Ardager", "Admin")
# # print(ardager.get_name())
#
# # print(User.get_base_role())

# 3. Декоратор @property

# class Product:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("price cannot be less than 0")
#         self.__price = value
#
# iphone = Product("Iphone 17 pro max", 1200)
#
# # print(iphone.price)
#
# print(iphone.price)
# iphone.price = -10
#

# Decorator
# Декоратор - это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность.

# def simple_decorator(func):
#     def wrapper():
#         print("before execute")
#         func()
#         print("after execute")
#     return wrapper
#
# @simple_decorator
# def greeting():
#     print("Hello world!!!")
#
# # greeting()
#
# def greeting_decorator(func):
#     def wrapper(name):
#         print(f"Hello {name}")
#         func(name)
#     return wrapper
#
# @greeting_decorator
# def greeting_name(name):
#     print(f"How are you {name} ?")
#
# # greeting_name("Ardager")
#
# def repeat_decorator(n):
#     def decorator(func):
#         def wrapper(name):
#             for i in range(n):
#                 func(name)
#         return wrapper
#     return decorator
#
# @repeat_decorator(5)
# def say_hello(name):
#     print(f"Hello {name}")
#
# say_hello("Ardager")

def class_decorator(cls):
    class NewClass(cls):

        def new_method(self):
            return "I am new method!!!"
    return NewClass

@class_decorator
class OldClass:

    def old_method(self):
        return "I am old method!!!"

obj_1 = OldClass()

print(type(obj_1))


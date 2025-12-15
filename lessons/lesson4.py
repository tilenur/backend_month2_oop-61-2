# Магические, статичные методы.
from _testcapi import MyList


# Dunder methods
# Магические методы - это специальные методы в Python, которые начинаются и
# заканчиваются двумя нижними подчеркиваниями:
# __init__,__str__, __add__, __eq__, __len__, __enter__, __exit__ и т.д.
# Они позволяют объектам вести себя как встроенные типы (числа, списки, строки).

class Test:

    def __init__(self, name="John Doe"):
        self.name = name

    def __str__(self):
        return self.name

my_obj = Test()

# my_str = "My str"
my_str = [1,22,3]

print(my_obj)
print(my_str)


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # +
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     # <
#     def __lt__(self, other):
#         return self.x < other.x
#
#     # >
#     def __gt__(self, other):
#         return self.x > other.x
#
#     # ==
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
# v1 = Vector(22, 22)
# v2 = Vector(23, 23)
#
# # <
# v3 = v2 < v1
# print(v3)  # False
#
# # +
# v4 = v2 + v1
# print(v4.x, v4.y)  # 45 45
#
# # >
# print(v2 > v1)     # True
#
# # ==
# print(v1 == v2)    # False
#
# test = int(15) + int(15)
# print(test)        # 30




# class MyList:
#
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#
# my_list = MyList()
# print(my_list.count)
# my_list()
# my_list()
# print(my_list.count)
#
# # from my_package import Hero, Test, add
#
# from my_package.module_2 import *
# # * - means all, but has an issue: takes all other imports which will result in errors
#
# from my_package.module_1 import add
#
# test = Test()
# # hero = Hero()
#
# mage_hero = MageHero()
# # print(add(12, 32))
#
#

# from colorama import Fore, Back, Style
#
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# import pandas as pd
#
# data = {
#   "Brand": ["Ford", "Ford", "Ford"],
#   "Model": ["Sierra", "F-150", "Mustang"],
#   "Typ" : ["2.0 GL", "Raptor", ["Mach-E", "Mach-1"]]
# }
# df = pd.DataFrame(data)
#
# newdf = df.explode('Typ')

# def find_element(my_list, target):
#     return my_list.index(target)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return print(mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return print("not found")

binary_search(my_list, target)

my_list_2 = [1, 2, 22, 3, 4, 3215, 3124, 5, 6, 7, 8, 9, 10]

print(my_list_2)
print(sorted(my_list_2))
import math
# 18

# def summ_unicode(first, second):
#
#     max_elemment = max(ord(first), ord(second))
#     min_elemment = min(ord(first), ord(second))
#
#     summ_unic = 0
#
#     for n in range(min_elemment, max_elemment + 1):
#         summ_unic = n + summ_unic
#     return summ_unic
#
# symbol_1 = str(input("Enter symbol 1: "))
# symbol_2 = str(input("Enter symbol 2: "))
#
# print(summ_unicode(symbol_1, symbol_2))


# 19

# def sum_of_all_numbers(number):
#
#     sum_of_number = 0
#
#     for degree in range(int(math.pow(1000000, 1 / number)) + 1):
#         degree = degree ** 3
#         sum_of_number = sum_of_number + degree
#
#     print("The sum of all numbers that are a power of:", sum_of_number)
#
# sum_of_all_numbers(3)

# 20
def find_number(number_1, number_2):

    for x in range(1000):

        if number_1 in str(x) and number_2 in str(x):
            print(x)

find_number('1', '7')
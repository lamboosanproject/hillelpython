import random

# 25
# def average(low_random, high_random):
#
#     array = []
#     count = 0
#     summa = 0
#
#     for i in range(low_random, high_random + 1):
#         item = random.randint(low_random, high_random)
#         array.append(item)
#         if item > 0:
#             count += 1
#             summa += item
#
#     if count != 0:
#         mean = summa / count
#         print(mean)
#         print(array)
#
#
# low_random = int(input("Enter start randomise list: "))
# high_random = int(input("Enter end randomise list: "))
#
# average(low_random, high_random)

# 26

# def difference_in_amounts(lists):
#     odd = 0
#     even = 0
#     result = 0
#     for x in lists:
#         if x % 2 == 0:
#             even += x
#         elif x % 2 != 0:
#             odd += x
#     result = even - odd
#     return result
#
# print(difference_in_amounts(lists))

# 27

# lists = []
#
# for i in range(50):
#     if i % 2 != 0:
#         lists.append(i)
# print(lists)
#
# a = random.shuffle(lists)
# print(lists)

# 28

# lists_1 = []
# lists_2 = []
#
# for i in range(0, 5 + 1):
#     item_1 = random.randint(0, 5 + 1)
#     item_2 = random.randint(0, 5 + 1)
#
#     lists_1.append(item_1)
#     lists_2.append(item_2)
#
# # output values
# print(lists_1, end="\n")
# print(lists_2)
#
# def sum_list(lst):
#
#     sum_lst = 0
#
#     for i in lst:
#         sum_lst += i
#     return sum_lst
#
# sum_list_1 = sum_list(lists_1)
# sum_list_2 = sum_list(lists_2)
#
# avr_1 = sum_list_1 / len(lists_1)
# avr_2 = sum_list_2 / len(lists_2)
#
# if sum_list_1 > sum_list_2:
#     print("Avr first list is greater")
# elif sum_list_1 < sum_list_2:
#     print("Avr second list is greater")
# else: print("Avr are equal")


# 29






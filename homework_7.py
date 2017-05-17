from random import randint

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
#
# print(lists)
#
# for i in range(len(lists) - 1):
#     j = random.randint(i + 1, len(lists) - 1)
#     x = lists[i]
#     lists[i] = lists[j]
#     lists[j] = x
#
# print(lists)

# Function create random list

def randomize_list(num, lower_limit, upper_limit):
    arrays = []
    for i in range(num):
        arrays.append(randint(lower_limit, upper_limit))
    return arrays

# 28

# def avr_list(array):
#     sum = 0
#     for elem in array:
#         sum += elem
#     return sum/len(array)
#
# def comparison(arr_1, arr_2):
#     if avr_list(arr_1) == avr_list(arr_2):
#         print("The average arithmetic lists are equal")
#     elif avr_list(arr_1) > avr_list(arr_2):
#         print("The arithmetic average of List 1 is greater")
#     elif avr_list(arr_1) < avr_list(arr_2):
#         print("The arithmetic average of List 2 is greater")
#
# array_1 = randomize_list(5, 0, 5)
# print("First array", array_1)
#
# array_2 = randomize_list(5, 0, 5)
# print("Second array", array_2)
#
# print('AVR first list =', avr_list(array_1))
# print('AVR second list =', avr_list(array_2))
#
# comparison(array_1, array_2)


# 29

# def frequency(lst):
#     count0 = 0
#     count1 = 0
#     count2 = 0
#
#     for elem in lst:
#         if elem == 0:
#             count0 += 1
#             continue
#         elif elem == 1:
#             count1 += 1
#             continue
#         elif elem == -1:
#             count2 += 1
#
#     if count0 > max(count1, count2):
#         print("The number 0 (zero) occurs most often:", count0)
#     elif count1 > max(count0, count2):
#         print("The number 1 (one) occurs most often:", count1)
#     elif count2 > max(count0, count1):
#         print("The number -1 (minus one) occurs most often:", count2)
#     else: print("Multiple numbers are repeated an equal number of times")
#
# lst = randomize_list(11, -1, 1)
# print(lst)
# frequency(lst)

# 30

# def string2list(line): #Перевод строки в список
#     lists = []
#     for i in range(len(line)):
#         lists.append(line[i])
#     return lists
#
# def encryption(user_line):
#
#     encrypt_text = ''
#
#     for i in range(len(user_line)):
#         id_char = encrypt.find(text[i])
#         if id_char + key < 0:
#             user_line[i] = encrypt[len(encrypt) + id_char + key]
#         elif id_char + key >= len(encrypt):
#             user_line[i] = encrypt[id_char - len(encrypt) + key]
#         else: user_line[i] = encrypt[id_char + key]
#
#     for i in range(len(user_line)):
#         encrypt_text += user_line[i]
#     print(encrypt_text)
#
# key = 5
# encrypt = "qwertyuioppasdfghjkl\'\\zxcvbnm1234567890QWERTYUIOPAASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю"
#
# text = input("Enter text")
# user_list = string2list(text)
# encryption(user_list)



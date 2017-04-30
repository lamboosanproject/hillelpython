import math, random

# 21

# number = int(input("Enter number: "))
# listing = [2]
#
# for i in range(3, number + 1, 2):
#     if (i > 10) and (i % 10 == 5):
#         continue
#     for j in listing:
#         if j * j - 1 > i:
#             listing.append(i)
#             break
#         if i % j == 0:
#             break
#     else: listing.append(i)
#
# print(listing)

# 22

# def twelve_digit_number(number):
#
#     print('Random number: ', number)
#     max_number = 0
#     number = str(number)
#
#     for y in number:
#
#         if int(y) > int(max_number):
#             max_number = int(y)
#
#     print("The largest figure: ", max_number)
#
# random_number = random.randint(int(1e11), int(1e12-1))
#
# twelve_digit_number(random_number)


# 23

# def recursion(number):
#
# # version 1
#     result = math.factorial(number)
#     print(result)
#
# # version 2
#     # for i in range(1, number + 1):
#     #     result *= i
#     # print(result)
#
# number = int(input('Enter number: '))
#
# recursion(number)

# 24
# number = 1
# unknown_number = random.randint(1, 10)
# print("The computer made a guess. Guess it.")
#
# while number != unknown_number:
#     number = int(input("Enter number:"))
#     if number > unknown_number:
#         print("Much")
#     elif number < unknown_number:
#         print("Few")
#     else:
#         print("Congratulations, you guessed")
#         break






# 1

# a = 2
# b = 2
# c = 2
#
# print((a + b * c) ** 2)

# 2

# a = 2
# b = 2
# c = 2
#
# print(a - 4 * b / c)

# 3

# a = 2
# b = 2
# c = 2
#
# print((a * b + 4) / (c - 1))

# 4

# def five_digit_number(number):
#
#     numbers = str(number)
#     listing = list(numbers)
#     comp = 1
#
#     for y in listing:
#         int_y = int(y)
#         if int_y % 2 != 0:
#             comp *= int_y
#     print(comp)
#
# random_number = int(input("Enter five digit number: "))
#
# five_digit_number(random_number)

# 5

# def nearest_to_10(b, c):
#     a = 10
#     abs_first = abs(b - a)
#     print(abs_first)
#     abs_second = abs(c - a)
#     print(abs_second)
#
#     if abs_first < abs_second:
#         print("The first numbers %.3f is closer to %.3f" % (b, a))
#
#     elif abs_first > abs_second:
#         print("The second numbers %.3f is closer to %.3f" % (c, a))
#
#     else: print("The numbers %.3f and %.3f are equidistant from %.3f" % (b, c, a))
#
# b = float(input("Enter firs number: "))
# c = float(input("Enter second number: "))
#
# nearest_to_10(b, c)

# 6
# import random
#
# number = 50
# listing = [2]
#
# for i in range(3, number + 1, 2):
#     if i > 10 and i % 10 == 5:
#         continue
#     for j in listing:
#         if j * j - 1 > i:
#             listing.append(i)
#             break
#         if i % j == 0:
#             break
#     else: listing.append(i)
#
# random.shuffle(listing)
# print(listing)


# 7

def fib(n):
    a = 0
    b = 1
    d = 0

    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        d += c
        print(c, end=' ')
    print("Summ = ", d)

fib(10)

# 8

# from random import random
# N = 15
# arr = [0]*N
# for i in range(N):
#     arr[i] = int(random()*100)
#     print(arr[i],end=' ')
# print()
#
# mn = min(arr)
# mx = max(arr)
#
# imn = arr.index(mn)
# imx = arr.index(mx)
# arr[imn], arr[imx] = arr[imx], arr[imn]
#
# for i in range(15):
#     print(arr[i], end=' ')

# 9



# 10

# table = []
# k = 10
# for line in range(8):
#     table.append([])
#     for columns in range(3):
#         table[line].append(k)
#         k += 1
#
# for line in table:
#     print(line)

# 11



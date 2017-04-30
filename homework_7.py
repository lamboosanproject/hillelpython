import random

# 25

# array = []
# low_random = int(input("Enter start randomise list: "))
# high_random = int(input("Enter end randomise list: "))
#
# count = 0
# summa = 0
#
# for i in range(low_random, high_random + 1):
#     item = random.randint(low_random, high_random)
#     array.append(item)
#     if item > 0:
#         count += 1
#         summa += item
#
#
# if count != 0:
#     mean = summa / count
#     print(mean)
#     print(array)
#

# 26

def difference_in_amounts(lists):
    odd = 0
    even = 0
    result = 0
    for x in lists:
        if x % 2 == 0:
            even += x
        elif x % 2 != 0:
            odd += x
    result = even - odd
    return result

print(difference_in_amounts(lists))






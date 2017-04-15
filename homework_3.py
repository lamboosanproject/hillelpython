import math
# 11

# radius = int(input('Enter radius: '))
#
# def degrees_to_radian(rad):
#     result = math.radians(rad)
#     return result
#
# print("Result radian = ", degrees_to_radian(radius))


# 12

# number = int(input('Enter number: '))
#
# def sum_number(numb = 111):
#     d1 = numb % 10
#     d2 = numb % 100 // 10
#     d3 = numb // 100
#     return d1 + d2 + d3
#
# print("Sum number = ", sum_number(number))

# 13

def area_and_perimeter(kat1, kat2):
    area = kat1 * kat2 / 2
    perimeter = math.sqrt(pow(kat1, 2) + pow(kat2, 2)) + kat1 + kat2
    return area, perimeter

area, perimeter = area_and_perimeter(int(input("Enter numb 1: ")), int(input("Enter numb 2: ")))

print("Area = ", area)
print("Perimeter = ", perimeter)




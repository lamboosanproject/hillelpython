from math import *

# 14

# number = int(input("Enter number: "))
#
# if number % 2 == 0:
#     print('The number is even')
# else: print('Odd number')

# 15

# x1 = float(input('Enter x1: '))
# y1 = float(input('Enter y1: '))
# radius_1 = float(input('Enter radius 1: '))
#
# x2 = float(input('Enter x2: '))
# y2 = float(input('Enter y2: '))
# radius_2 = float(input('Enter radius 2: '))
#
# def is_circles_intersect():
#     center_distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
#     result = center_distance - (radius_1 + radius_2)
#     return result <= 0
#
# print("Is circles intersect?:", is_circles_intersect())

# 16

# first_train = float(input('Enter speed first train: '))
# second_train = float(input('Enter speed second train: '))
# first_train_time = 4 / first_train
# second_train_time = 6 / second_train
#
# if first_train_time < second_train_time:
#     print("Trains will not collide")
# else:
#     print("Trains will collide")

# 17

def solve_quadratic_equation(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c
    if discriminant > 0:
        x1 = (-b - sqrt(discriminant)) / (2 * a)
        x2 = (-b + sqrt(discriminant)) / (2 * a)
    elif discriminant == 0:
        x1 = x2 = (-b) / (2 * a)
    elif discriminant < 0:
        x1 = x2 = None
    return x1, x2

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

print("The result for a = %d, b = %d and c = %d is:" % (a, b, c), solve_quadratic_equation(a, b, c))



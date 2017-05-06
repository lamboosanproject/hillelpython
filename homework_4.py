from math import *

# 14

# number = int(input("Enter number: "))
#
# if number % 2 == 0:
#     print('The number is even')
# else: print('Odd number')

# 15

def is_circles_intersect(x1, y1, radius_1, x2, y2, radius_2):
    import math

    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    radius = radius_1 + radius_2
    if distance <= radius or distance < (math.fabs(radius_1 - radius_2)):
        print("Circles are intersected")
    else:
        print("Do not intersect")

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
radius_1 = float(input('Enter radius 1: '))

x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
radius_2 = float(input('Enter radius 2: '))

is_circles_intersect(x1, y1, radius_1, x2, y2, radius_2)

# 16

# def will_the_trains(first_train,second_train):
#
#     first_train_time = 4 / first_train
#     second_train_time = 6 / second_train
#     if first_train_time < second_train_time:
#         print("Trains will not collide")
#     else:
#         print("Trains will collide")
#
# first_train = float(input('Enter speed first train: '))
# second_train = float(input('Enter speed second train: '))
#
# will_the_trains(first_train, second_train)

# 17
#
# def solve_quadratic_equation(a, b, c):
#     discriminant = pow(b, 2) - 4 * a * c
#     if discriminant > 0:
#         x1 = (-b - sqrt(discriminant)) / (2 * a)
#         x2 = (-b + sqrt(discriminant)) / (2 * a)
#     elif discriminant == 0:
#         x1 = x2 = (-b) / (2 * a)
#     elif discriminant < 0:
#         x1 = x2 = None
#     return x1, x2
#
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))
#
# print("The result for a = %d, b = %d and c = %d is:" % (a, b, c), solve_quadratic_equation(a, b, c))
#
#

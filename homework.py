import math

# 1
a = 3
b = 7
c = 10

result = a + b * (c / 2)
print("The result of job expression 1: %d " % result)

# 2

a2 = 3
b2 = 6

result_2 = (a2**2 + b2**2) % 2
print("The result of job expression 2: %d " % result_2)

# 3

a3 = 10
b3 = 20
c3 = 30

result_3 = (a3 + b3) / 12 * c3 % 4 + b3
print("The result of job expression 3: %d " % result_3)

# 4

a4 = 8.8
b4 = 7.3
c4 = 4.2

result_4 = (a4 - b4 * c4) / (a4 + b4) % c4
print("The result of job expression 4: %.4f " % result_4)

# 5


a5 = 12
b5 = -27
c5 = 42

result_5 = (math.fabs(a5 - b5) / (a5 + b5)**3 - math.cos(c5))
print("The result of job expression 5: %.3f " % result_5)

#6

a6 = 1
b6 = -2
c6 = 5

result_6 = ((math.log10(1 + c6) / -b6)**4 + math.fabs(a6))
print("The result of job expression 6: %f " % result_6)






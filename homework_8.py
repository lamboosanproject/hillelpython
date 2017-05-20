from random import choice, randint

# 31
length = int(input('Enter length password: '))

char = list('_123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

print(''.join([choice(char) for x in range(length)]))






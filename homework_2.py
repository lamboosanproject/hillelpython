# 7

# d = "05.17.2016"

# month = d[0:2]
# days = d[3:5]
# years = d[6:]
# print("%s.%s.%s" % (days, month, years))

# 8

# text_1 ="Say 'Syntax Error' and i dare you. i double dare you"
# text_2 ="Syntax Error"

# quantity_1 = text_2[:len(text_2) // 2]
# quantity_2 = text_2[len(text_2) // 2 :]

# text_3 = quantity_1 + text_1 + quantity_2

# print(text_3)

# quantity_3 = text_1[:len(text_1) // 2]
# quantity_4 = text_1[len(text_1) // 2 :]

# print(quantity_3 + text_3 + quantity_4)


# 9

text_1 = 'hall of fame'

splits_1, splits_2, splits_3 = text_1.split(' ')

print(splits_1, splits_2.upper(), splits_3)

# 10

# text_3 = "Leo Tolstoy*1828-08-28*1910-11-20"

# split_1, split_2, split_3 = text_3.split('*')

# birth_year, birth_month, birth_day = split_2.split('-')
# death_year, death_month, death_day = split_3.split('-')

# years = int(death_year) - int(birth_year)

# print("%s, %d" % (split_1, years))


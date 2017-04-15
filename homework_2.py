# 7

# d = "05.17.2016"
#
# month = d[0:2]
# days = d[3:5]
# years = d[6:]
# print("%s.%s.%s" % (days, month, years))

#8

# text_1 ="Say 'Syntax Error' and i dare you. i double dare you"
# text_2 ="Syntax Error"
#
# print("Кол символов в строке 1:", len(text_1))
# print("Кол символов в строке 2:", len(text_2))
#
# text_3 = text_2[:6], text_1, text_2[7:]
#
# print(text_1[:26], text_3, text_1[26:])

# 9

# text_1 = 'hall of fame'
#
# find_text = text_1.find(' ')
#
# concat = find_text + text_1[find_text + 1 :].find(' ') + 1
# text_2 = text_1[find_text + 1 : concat]
#
# print(text_1[: find_text + 1] + text_2.upper() + text_1[concat :])

# 10

text_3 = "Leo Tolstoy*1828-08-28*1910-11-20"

split_1, split_2, split_3 = text_3.split('*')

birth_year, birth_month, birth_day = split_2.split('-')
death_year, death_month, death_day = split_3.split('-')

years = int(death_year) - int(birth_year)

print("%s, %d" % (split_1, years))


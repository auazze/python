# # name = input()
# # print(f'Hi, {name}')
#
# #
# # ЧИСЛА - INTEGERS
# #
#
# # Узнаём тип данных
# print(type(6 / 3))
#
# # Деление с округлением до целого - целочисленное деление
# print(2 // 4)
# print(5 // 4)
#
# # % - остаток от деления
# print(5 % 2.5)
# print(50 % 5)
#
# # округление
# print(round(5.75))
# print(round(5.15))
#
# # complex - bin or decimal - бинарные или десятичные
# print(bin(5))
# print(int("0b101", 2))  # используя int - 2 - переведёт двоичное (какое и указано) в десятичную
# print(int("5", 10))  # используя int - 10 - десятичное, так и напишет
#
# #
# # var - Variables - вариативность
# #
#
# iq = 190
# iq = "one hundred and ninty"
# my_iq = 50
# print(f"""{iq}
# {my_iq}""")
#
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
#
# #
# # Augmented Assignment Operator
# #
#
# # instead of
# some_value = 5
# some_value = some_value + 2
# print(some_value)
#
# # using +=
# some_value = 5
# some_value += 2     # отнимаем 2 от значения этого some_value
# some_value *= 2     # здесь идём по порядку - 5+2=7, 7*2=14
# print(some_value)
# # Это не равно 5+2*2, ведь получится 9
#
# #
# # My favorite strings
# #
#
# # strings concatenation - we know it
# print("Hey,"+" "+"What ya"+" "+"doing?")
#
#
#
# # type conversion
# a = str(100)
# b = int(101)
# c = type(b)
# print(c, type(a))
#
# # escape sequence and tabulation and new_line
# weather = "\t It\'s \"kind of\" sunny \n hope you have a good day"
# print(weather)
#
# # f-string - formatted string
# name = "Stepan"
# time = 2
# # use this!
# print(f"Oh my gosh, {name}! How you have been for that {time} years ???")
#
# # instead of this nightmare
# print("Oh my gosh, " + name + "! How you have been for that " + str(time) + " years ???")
# # and instead of this
# print("Oh my gosh, {}! How you have been for that {} years ???".format("Stepan", "2"))
# # or this
# print("Oh my gosh, {}! How you have been for that {} years ???".format(name, time))
# # or thiiis
# print("Oh my gosh, {0}! How you have been for that {1} years ???".format(name, time))
# # and no way for this
# print("Oh my gosh, {new_name}! How you have been for that {new_time} years ???".format(new_name="Stefan", new_time=5))
#
#
# # string indexing
# selfish = "me me me"
# # _________01234567
# # string slicing - [start:stop:stepover]
# print(selfish[0:8:1])
# # step over
# print(selfish[::3])
# # reverse
# print(selfish[::-1])
#
# # immutability
# selfish = "X"
# # selfish[0] = "8"        # error, cuz strings - immutable
# selfish += "8"
# print(selfish)
#

#
# built-in functions and methods
#
greet = "hello"
print(len(greet))     # get number of length
print(greet[:])     # from start to finish - without [:] at all
print(greet[0:len(greet)])      # the same - from start to the all length of the "greet" - to finish

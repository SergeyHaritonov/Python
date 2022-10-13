# Задача 0. Дано число N. Найти все его делители. Для
# каждого делителя укажите чётный он или нечётный.
# 10 -> 10 (чётный), 5(нечётный), 2 (чётный),
# 1(нечётный) 

# Делитель - это число на которое число N делится без остатка.
# Все делители лежат в пределах от 1 до половины заданного числа + само заданное число.

# def Zadacha0():
#     number = 60
#     for i in range(1, number + 1):
#         if number % i == 0:
#             print(i, end = ' ')
#             if i % 2 == 0:
#                 print('- четный')
#             else:
#                 print('- нечетный')
# Zadacha0()

# -----------------------------------------------------------------------------------------------

# Создадим для каждого действия отдельный метод.

import numbers


def CheckEven(x):
    if x % 2 == 0:
        return '- четный'
    else:
        return '- нечетный'



def Zadacha0():
    number = 60
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end = ' ')
            print(CheckEven(i))
# Zadacha0()

# ----------------------------------------------------------------------------------------------------

# Задача 1. Выведите таблицу истинности для
# выражения ¬ X ∨ Y.

#   X       Y      ¬ X ∨ Y
#   0       0          1
#   0       1          1
#   1       0          0
#   1       1          1

# print('x | y | ¬ X ∨ Y')
# for x in range(0, 2):
#     for y in range(0, 2):
#         sum = not x or y
#         print(f'{x} | {y} | {int(sum)}') # Можно вместо int использовать bool, тогда в print выведется True и False.


# -----------------------------------------------------------------------------------------------------------------------

# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки 
# в другую.

# «qwe» «qwertyqwe» -> 2 

# string1 = input('Введите первую строку: ')
# string2 = input('Введите вторую строку: ')
# count = 0

# if len(string1) > len(string2):
#     for i in range(len(string1)):
#         # print(string1[i:i+len(string2)])
#         if string2 == string1[i:i+len(string2)]:
#             count+=1
#     print(string2, string1, '->', count)


# else:
#     for i in range(len(string2)):
#         # print(string2[i:i+len(string1)])
#         if string1 == string2[i:i+len(string1)]:
#             count+=1
#     print(string1, string2, '->', count)

# -----------------------------------------------------------------------------------------------------

# Решение 2

# str1 = input('Enter text1: ')
# str2 = input('Enter text2: ')
# if len(str1) > len(str2):
#     print(f'Text1 include text2 {str1.count(str2)} times')
# else:
#     print(f'Text2 include text1 {str2.count(str1)} times')


# ---------------------------------------------------------------------------------------------------------

# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...
# N = 5 -> [1, -3, 9, -27, 81]


# stepen = int(input('Введите число: '))
# number = -3
# numbers = [i for i in range(stepen)]
# for i in range(0, stepen):
#     numbers[i] = number**i
# print(f'N = {stepen} -> ', numbers)

# stepen = int(input('Введите число: '))
# numbers = []
# for i in range(0, stepen):
#     numbers.append((-3)**i) # append добавляет в список значения, которое указано в круглых скобках.
# print(f'N = {stepen} -> ', numbers)

# ---------------------------------------------------------------------------------------------------------------


# Задача 4. Найдите все числа до 10000, у который количество делителей равно 10. 
# list = []
# count = 0
# for i in range(1, 10001):
#     for j in range(1, 10001):
#         if j % i == 0:
#             count+=1
#     print(count)
#     if count == 10:
#         list.append(j)
# print(list)

def check_number(n):
    divigers = list()
    for diviger in range(1, int(n ** 0.5)):
        if n % diviger == 0:
            divigers.append(diviger)
    return len(divigers) == 5


def find_numbers():
    numbers = list()
    for i in range(1, 10_001):
        if check_number(i):
            numbers.append(i)
    return numbers


def main():
    print(find_numbers.__doc__)
    print(check_number.__doc__)
    print(*find_numbers())


if __name__ == '__main__':
    main()
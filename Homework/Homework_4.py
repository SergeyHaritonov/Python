# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def Multipliers():
    num = int(input('Введите число: '))
    number = num
    dividers = []
    i = 2
    while num > 1:
        if num % i == 0:
            dividers.append(i)
            num = num / i
        else:
            i += 1
    print(f'Простые множители числа {number}:', *dividers, sep='  ')

Multipliers()


# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»


def Open_File(nameFile, i):
    f = open(nameFile, encoding='utf-8')
    phrase = f.readlines()
    f.close()
    phrase = [i.strip() for i in phrase]
    list = phrase[i].split(', ')
    return set(list)

assortment = Open_File('Icecream.txt', 0)
in_stock = Open_File('Icecream.txt', 1)

print(*list(assortment), sep=', ')
print(*list(in_stock), sep=', ')

diff = assortment.difference(in_stock)

print(f'Закончилось: ', *list(diff))



# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа. 
# 3 -> 3.142    5 -> 3.14159

import math

print(round(math.pi, int(input('Введите число знаков после запятой: '))))



# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x  2. 3x^2 + x + 8 Результат: 8x^2 + 4x + 8


# Эту задачу своей головой не осилил. Нашел в инернете, что можно через бибилиотеку решить


from sympy import Symbol, collect

s1="5*x**2 + 3*x"
s2='3*x**2 + x + 8'

x=Symbol('x')
s3= collect(s1 + '+' + s2, x)
print(s3)

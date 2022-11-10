# Задача 0. Дан список случайных элементов. Проверьте, что все его элементы уникальны.

# [7, 2, 4, 1, 6] –> да
# [7, 2, 4, 2, 6] -> нет

import random

numbers = [random.randint(1, 10) for i in range(5)]
print(numbers)

setNumbers = list(set(numbers))
print(setNumbers)

# Variant 1

if (len(numbers) == len(setNumbers)):
    print(f'{numbers} -> да')
else:
    print(f'{numbers} -> нет')

# Variant 2

print(f"все элементы уникальны -> {numbers} {setNumbers}" if len(numbers) == len(setNumbers) else f"есть совпадающие элементы -> {numbers} {setNumbers}")


# ----------------------------------------------------------------------------------------------------------------------------------------------


# Задача 1. Даны два случайных пятизначных числа. Определить, состоят ли они из одних и тех же цифр.

# 72426, 27624 –> да
# 44444, 44441 -> нет


import random
from collections import Counter

number1 = str(random.randint(10000, 99999))
number2 = str(random.randint(10000, 99999))
# print(number1, number2)

number1List = dict(Counter(number1))
number2List = dict(Counter(number2))
# print(number1List, number2List)

print(f"да -> {number1} {number2}" if number1List == number2List else f"нет -> {number1} {number2}")


# ДЕНИС

def CheckNumber(number):
    return 10000 <= number <= 99999


def CountAllElements(number):
    number = str(number)
    number = set((i, number.count(i)) for i in set(number)) # Создаем множество кортежей
    print(number)
    return number

numberFirst = 72426
numberSecond = 27624
print(set(str(numberFirst)))
print(set(str(numberSecond)))

if CheckNumber(numberFirst) and CheckNumber(numberSecond):
    numberFirst = CountAllElements(numberFirst)
    numberSecond = CountAllElements(numberSecond)
    
    print("yes" if numberFirst == numberSecond else "no")
else:
    print("числа не удовлетворяют условию")

# ----------------------------------------------------------------------------------------------------------------------------------------


# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. Приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких действий.
# в) Решите задачу средствами Python

# 2+2 => 4 
# 1+2*3 => 7



#                                           а)


def sum(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2


formula = input('Введите арифметическое выражение: ')
formulaElements = []
number = ''
operator = ''

for i in formula:
    if i.isdigit():
        number += i
    else:
        formulaElements.append(int(number))
        operator = i
        number = ''
formulaElements.append(int(number))
print(formulaElements)
print(operator)

# Создаем словарь операций

operations = \
    {
        '+': sum(formulaElements[0], formulaElements[1]),                   # Либо так   '+': formulaElements[0] + formulaElements[1],
        '-': minus(formulaElements[0], formulaElements[1]),                 # Либо так   '-': formulaElements[0] - formulaElements[1],
        '*': multiply(formulaElements[0], formulaElements[1]),              # Либо так   '*': formulaElements[0] * formulaElements[1],
        '/': division(formulaElements[0], formulaElements[1]),              # Либо так   '/': formulaElements[0] / formulaElements[1],
    }

print(operations[operator])


#                                                       б)

# Решать через filter   (filter на умножение, потом filter на плюс и т.д.) Минусы заменить на +-




#                                                       в)


formula = '20*33'
print(formula, '=', eval(formula))


# --------------------------------------------------------------------------------------------------------------------------




# Задача 3. Имеется 1000 рублей. Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?



bullPrice = 100
cowPrice = 50
calfPrice = 5
money = 1000

for bullCount in range(money//bullPrice): # // Целочисленное деление, возвращает результат в формате int
    for cowCount in range(money//cowPrice):
        for calfCount in range(money//calfPrice):
            if bullCount + cowCount + calfCount == 100 and bullCount * bullPrice + cowCount * cowPrice + calfCount * calfPrice == 1000:
                print(f'быки {bullCount}, коровы {cowCount}, телята {calfCount}')



# --------------------------------------------------------------------------------------------------------------------------------------------



# Задача 4. Дан список, выведите его первый и последний элементы.



import random

numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
print(numbers[0], numbers[-1])

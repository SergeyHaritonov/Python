# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

numbers = [random.randint(1, 10) for i in range(10)]
print(*numbers)

numbers_above_five = list(filter(lambda x: x > 5, numbers))
print(*numbers_above_five)


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


import random

element = int(input('С какого элемента от 1 до 20 начать последовательность?  '))

numbers = [random.randint(1, 30) for i in range(20)]
print(numbers)

def Increasing(nums):
    i = element - 1
    increasing_list = [nums[i]]    
    for i in range(i, len(nums)):
        if nums[i] > max(increasing_list):
            increasing_list.append(nums[i])
    return increasing_list
    
print(Increasing(numbers))


# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.

# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random
from collections import Counter

numbers = [random.randint(1, 10) for i in range(10)]

myList = dict(Counter(numbers))

values = list(myList.values())

unic_elements = list(set(numbers))

def CountingRepeatElements(values):
    sum = 0
    for i in range(len(values)):
        if values[i] > 1:
            sum = sum + values[i]
    return sum

print(f'Изначальный список элементов -> {numbers}')

print(CountingRepeatElements(values), 'элемента(-ов) совпадают')

print(F'Список уникальных элементов {unic_elements}')


#  На 4 задачу времени не хватило.
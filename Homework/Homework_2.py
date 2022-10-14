# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# from math import factorial

def InputNumber():
    number = int(input('Введите число: '))
    return number

def Factorial(number):
    list = [] 
    factorial = 1      
    for i in range(1, number+1):
        factorial *= i
        list.append(factorial)
    print(f'N = {number} ->', list)
    
# Factorial(InputNumber())    



# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def TruthTable():
    print('x | y | z | ¬(X ∧ Y) ∨ Z')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                sum = not (x and y) or z
                print(f'{x} | {y} | {z} | {int(sum)}')

# TruthTable()


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


Денис, не смог обернуть всё это в методы, чтобы они корректно возвращали значения и работали.
Если не сложно, покажите как это сделать.

# string1 = input('Введите первую строку: ')
# string2 = input('Введите вторую строку: ')

# count = 0

# len1 = len(string1)
# len2 = len(string2)

# if len1 <= len2:
#     for i in range(len1):
#         for j in range(len2):
#             if string1[i] == string2[j]:
#                 count+=1
#         print(f'{string1[i]} - {count}', end='  ')
#         count = 0

# else:
#     for i in range(len2):
#         for j in range(len1):
#             if string2[i] == string1[j]:
#                 count+=1
#         print(f'{string2[i]} - {count}', end='  ')
#         count = 0



# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]


number = int(input('Введите число: '))
count = int(input('Веведите число шагов для сдвига: '))
list = [i for i in range(-number, number+1)]
length = len(list)
print(list)

def Shifting(arr, count):
    for i in range(length - count):
        arr = arr[1:] + arr[:1]
    return arr
    

# print(Shifting(list, count))

# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN
# N может быть любой длины.

# N = 132: 132 + 132132 + 132132132 = 132264396


N = 132

print(f'N = {N}: {N} + {int(str(N) * 2)} + {int(str(N) * 3)} = {N + int(str(N) * 2) + int(str(N) * 3)}')



# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.


# {0, 5, 6, 2, 7, 7, 8, 1, 1, 9} - 277 -> да
# {4, 4, 3, 6, 7, 0, 8, 5, 1, 2} - 812 -> нет


import random

array = [random.randint(0, 9) for i in range(15)]
print(array)

number = input('Введите натуральное трехзначное число: ')
numberList = []


for i in number:
    numberList.append(int(i))
print(numberList)

def Checking(arr):
    for i in range(len(arr)-2):
        if arr[i] == numberList[0] and arr[i+1] == numberList[1] and arr[i+2] == numberList[2]:
            isMatch = True
            break
        else:
            isMatch = False
    return isMatch

def PrintingResult(smth):
    if smth:
        print(f'{array} - {number} -> да')
    else:
        print(f'{array} - {number} -> нет')

isMatch = Checking(array)

PrintingResult(isMatch)




# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.


numerator = 11
denominator = 11

for i in range(1, numerator):
    print()
    for j in range(2, denominator+1):
        if i < j:
            if (i%2 != 0 or j%2 !=0) and (i%3 != 0 or j%3 !=0) and (i%5 != 0 or j%5 !=0):
                print(f'{i} / {j}')
        

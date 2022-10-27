# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. Заполните список случайным образом числами от 1 до 100.

# import random

# data = [random.randint(1, 100) for i in range(15)]

# print(data)

# data = list(filter(lambda e: not e % 5, (random.randint(1, 100) for i in range(15))))

# print(data)


# ----------------------------------------------------------------------------------------------------------------------------------------



# Задача 1. На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа, увеличенных на 10.

# 9650 –> [19, 16, 15, 10]
# 1043 –> [11, 10, 14, 13]

# number = input('Введите число: ')

# number = list(map(int, number)) # Переводит строку в число и записывает в список

# number_list = list(map(lambda e: e + 10, number))

# print(number)
# print(number_list)

# # 2 вариант

# number = list(input('Введите число: ')) # Сразу получаем список символов из введенной строки
# print(number)
# plus_ten = lambda x: int(x) + 10

# number = list(map(plus_ten, number))
# print(number)


# -----------   Решение в одну строку   -----------------------------------------------------------------

# print(list(map(lambda e: e + 10, list(map(int, input('Введите число: '))))))


# --------------------------------------------------------------------------------------------------------------------------------------------


# Задача 2. В зоопарк отправили отчёт о новом поступлении зверей с ошибкой, в результате которой некоторые данные не расшифровались.
# Расшифруйте данные. Определите, в какой клетке находится лев. Номер клетки совпадает с номером строки.

# Файл animals.txt

# абвгдеёжзийклмнопрстуфхцчшщъыьэюя

# Каждая буква кодируется 6 символами (например, а - 000000; б - 000001 и т.д.), потому что в один бит можно поместить 2 символа (0 или 1),
#                       0 0
# в 2 бита - 4 символа  0 1    в  3 бита - 8, в 4 - 16 и т.д. Соответственно  33 буквы алфита поместятся в 6 бит, поэтому 6 символов.
#                       1 0
#                       1 1
# 000000 - это цифра 1 в десятичном представлении, 000001 - цифра 1, 000010 - цифра 2. Коды букв совпадают с индексами букв в переменной alphabet

# Надо расшифровать буквы в файле animals.txt. 1 буква - 6 символов.


# def ConvertToBinary(number):
#     result = ''
#     while number > 0:
#         result = str(number%2) + result # Такая конструкция позволяет записывать получившееся число в обратном порядке.
#         number =number // 2
#     return result

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# codeList = [int(i) for i in range(len(alphabet))]

# # print(codeList)

# # n = int('100111111111111', 2)  # Переводит число в кавычках в выбранную систему исчисления. Цифра 2 после запятой - в двоичную??? Не уверен

# codeList = [ConvertToBinary(i) for i in codeList]
# # print(codeList)

# codeList = ["0"*(6-len(i)) + i for i in codeList] # Эта конструкция добавляет впереди нули, но в зависимости от длины двоичного представления
#                                               # числа i добавляет столько нулей, что в итоге всё число имеет в длину 6 символов.
# # print(codeList)

# dictionary = {}                 # Создаем словарь, в котором ключ - двоичное представление буквы, значение - сама буква.
# for i in range(len(codeList)):
#     dictionary[codeList[i]] = alphabet[i]
# print(dictionary)

# data = open('animals.txt', 'r')
# animalCodeList = data.readlines()
# data.close()
# # print(animalCodeList)

# for animal in animalCodeList:
#     for i in range(len(animal)//6): # находим сколько букв зашифровано в строке
#         bias = i * 6 # Переменная, чтобы считать сдвиги для срезов
#         # print(animal[bias:bias+6], end='') # Последний срез не включается, т.е в первой итерации bias = 0, bias + 6 = 5 (0,1,2,3,4,5 всего 6 проходов)
#         print(dictionary[animal[bias:bias+6]], end='')
#     print()


# ---------------------------------------------------------------------------------------------------------------------------------------------


# Задача 3. Имеется информация о том, телефонами каких компаний сейчас торгуют магазины. 
# Определите те компании, чьи телефоны присутствуют в каждом магазине.


# data = open('phones.txt', 'r')
# phones = data.readlines()
# data.close()

# shop1 = set(phones[1].replace('\n', '').split(', ')) # replace заменяет первый символ на второй символ, указанные в скобках
# # Без replace вывод был таким: в конце списка есть символ переноса строки
# # ['ShEXP', 'ShLG', 'Shigma', 'ShTE', 'Shalcatel', 'Shericsson', 'Shpanasonic', 'Shony', 'ShTC', 'Shirbis', 'Shmotorola', 'SheXet', 'Shapple\n']
# shop2 = set(phones[3].replace('\n', '').split(', '))
# shop3 = set(phones[5].split(', '))
# print(shop1)
# print(shop2)
# print(shop3)
# print(shop1.intersection(shop2).intersection(shop3))


# -----------------------------------------------------------------------------------------------------------------------------------------------



# Задача 4. Задайте список из 15 случайных чисел. Выведите все пары кратных чисел из этого списка.

import random

list = [random.randint(1, 20) for i in range(15)]
print(list)


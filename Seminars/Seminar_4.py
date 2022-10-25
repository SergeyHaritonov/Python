# Задача 0. Создайте файл random.txt. Запишите в него 10 случайных чисел


import random

print(random.random()) # Диапазон от 0 до 1 генерирует дробную часть случайного числа

for i in range(10): # Сгенерирует заданное количество случайных чисел
    print(random.randint(1, 10)) # Генерирует случайное целое число из заданного промежутка, включая обе границы(10 тоже выпадет)

# # Чтобы поместить цифры в список:

numbers = []
for i in range(10): 
    numbers.append(random.randint(1, 10))
print(numbers)


numbers = [0] * 10 # Задает список из 10 элементов, заполненный нулями
for i in range(10): 
    numbers[i] = random.randint(1, 10) # Присваиваем i'тому элементу списка рандомное значение
print(numbers)

# Заранее файл random.txt создавать не надо. Он появится сам после выполнения команды:

# По умолчанию open открывает файл для чтения, поэтому вылезет ошибка, т.к. файла random.txt пока не существует.
# Доп. параметр 'w' открывает файл для записи, поэтому создает его, если его пока нет, даже если просто написать data = open('random.txt', 'w')
# data = open('random.txt', 'w')
# data.writelines(str(numbers)) # Обязательно переводить данные в строку. writelines принимает только строки
# data.close()

# Другой способ покороче

# with open('random.txt', 'a') as data:
#     data.writelines(str(numbers) + '\n') # Обязательно переводить данные в строку. writelines принимает только строки.
                                           # \n позволяет печатать каждую строку с новой строки.
# Закрывать файл не надо

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 1. Создайте кортеж, заполненный случайными числами. Напишите метод, который заменяет элемент в кортеже по заданному индексу.

# import random

# def Change_Index(numbers, index):
#     numbers = list(numbers) # Переводим кортеж в список. В списке менять элементы можно
#     numbers[index] = random.randint(10, 100)
#     numbers = tuple(numbers)
#     return numbers

# size = random.randint(5, 12) # Задаем рандомно размер кортежа
# numbers = tuple(random.randint(10, 100) for i in range(size)) # Задаем кортеж

# print(numbers)

# index = int(input('Введите номер индекса для замены: '))

# print(Change_Index(numbers, index))


# --------------------------------------------------------------------------------------------------------------------------------


# Задача 2. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные». На главную роль нужен актёр
# обладающий всеми тремя качествами. Определите, сколько есть претендентов на главную роль. Списки актёров поместите в
# соответствующие файлы.

# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад


# РЕШЕНИЕ, ЕСЛИ В ФАЙЛАХ ДАННЫЕ ЗАПИСАНЫ В НЕСКОЛЬКО СТРОК. READLINES СЧИТЫВАЕТ НЕСКОЛЬКО СТРОК


# handsome = set()
# smart = set()
# strong = set()

# with open('handsome.txt', encoding='utf-8') as inf:
#     for line in inf.readlines():
#         handsome.add(line.rstrip())
# print(handsome)

# with open('smart.txt', encoding='utf-8') as inf:
#     for line in inf.readlines():
#         smart.add(line.rstrip())
# print(smart)

# with open('strong.txt', encoding='utf-8') as inf:
#     for line in inf.readlines():
#         strong.add(line.rstrip())
# print(strong)

# print(*(handsome & smart & strong), sep='\n')

# for el in handsome & smart & strong:
#     print(el)

# РЕШЕНИЕ, ЕСЛИ В ФАЙЛАХ ДАННЫЕ ЗАПИСАНЫ В ОДНУ СТРОКУ

with open('handsome.txt', encoding='utf-8') as inf:
    handsome = set(inf.readline().rstrip().split())
print(handsome)

with open('smart.txt', encoding='utf-8') as inf:
    smart = set(inf.readline().rstrip().split())
print(smart)

with open('strong.txt', encoding='utf-8') as inf:
    strong = set(inf.readline().rstrip().split())
print(strong)

print(*(handsome & smart & strong), sep='\n')

for el in handsome & smart & strong:
    print(el)


# РЕШЕНИЕ ДЕНИСА

# def Open_File(nameFile):
#     f = open(nameFile, encoding='utf-8')
#     phrase = f.readlines()
#     f.close()
#     list = phrase[0].split() # Берем первую строку файла и разбиваем ее на состовляющие через пробел. В этом файле строка единственная
#     return set(list)

# handsome = Open_File('handsome.txt')
# smart = Open_File('smart.txt')
# strong = Open_File('strong.txt')

# print(handsome)
# print(smart)
# print(strong)

# print(handsome.intersection(smart).intersection(strong))



# -------------------------------------------------------------------------------------------------------------------------


# Задача 3. Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов. Удалите из списка дубликаты уже имеющихся элементов.

# [1, 2, 9, 5, 2, 18, 3, 5, 13, 2] -> [1, 2, 9, 5, 18, 3, 13]

# import random


# numbers = [random.randint(1, 20) for i in range(10)]
# print(numbers)

# numbers = set(numbers) # При переводе в set() список автоматически убирает дублирующиеся элементы и сортирует их по возрастанию.

# print(numbers)

# -----------------------------------------------------------------

# print(list(set(list(random.randint(1, 20) for _ in range(10))))) # Решение в одну строку


# -----------------------------------------------------------------------------------------------------------------------------------------


# Задача 4. Дано число N. Найдите площадь круга с радиусом N. Ответ округлите до сотых.

# import math

# radius = int(input('Введите число: '))

# print(round(math.pi * math.pow(radius, 2), 2))
# pow - возведение в степень(после radius указывается степень), цифра после round указывает количество знаков после запятой для округления
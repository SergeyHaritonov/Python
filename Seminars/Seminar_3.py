# Задача 0. Создайте скрипт func и функцию чтения последней строки файла. Вызовите её из скрипта example.

# import example

# example.ReadLastRow()


# Задача 1. Дан файл, заполненный числами построчно. Считайте файл. Выведите все элементы, стоящие на чётных строках, а потом на нечётных.


from re import I


def Number():
    data = open('Zadacha1.txt', encoding='utf-8')
    numbers = data.readlines()
    data.close()
    for i in range(len(numbers)): # Можно указать range(0, len(numbers), 2) парметры цикла от 0 до len(numbers) с шагом 2, 
                                    # будет сразу печатать только четные строки. И тогда можно убрать проверку if'ом.
        if i % 2 == 0:
            print(numbers[i], end='')
    print()
    for i in range(len(numbers)): # Тогда здесь range(1, len(numbers), 2)
        if i % 2 != 0:
            print(numbers[i], end='')
# Number()


# Задача 2. При работе с документацией менеджер допустил ошибку, названия товаров перемешались с ценами. Помогите восстановить документ. 
# Порядковый номер товара совпадает с номером цены.

# туфли рубашка 2000 1000 шарф юбка шорты 1500 3000 сапоги 500 5000 брюки 1500 2000 свитер 

# туфли 2000
# рубашка 1000
# шарф 1500
# юбка 3000
# шорты 500
# сапоги 5000
# брюки 1500
# свитер 2000


# file = open('Zadacha2.txt', encoding='utf-8')
# data = file.readline()
# file.close()
# clothes = []
# prices = []
# data = data.split()
# for i in data:
#     if i.isdigit():
#         prices.append(i)
#     else:
#         clothes.append(i)     
# for i in range(len(prices)):
#     print(clothes[i] + ' ' + prices[i])


# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из букв и чисел. Создайте скрипт для сохранения пароля в файл password.txt




# Задача 4. Считайте строковые данные из файла. Создайте словарь, содержащий все символы в файле.


data = open('Zadacha2.txt', encoding='utf-8')
string1 = data.read() # Команда read считывает весь файл в одну строку и не не нужно делать конвертацию из списка в строку для цикла for
data.close()
dictionary = {}
for i in string1:
    dictionary[i] = i
print(dictionary)

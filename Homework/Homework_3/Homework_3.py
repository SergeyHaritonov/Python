# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8



def Fibbonacci(): 
    n = int(input('Введите число: '))   
    x = [1,1]
    for i in range(2, n):
        x.append(x[-1] + x[-2])
    x = ', '.join(str(i) for i in x)
    print(x)
    return x

data = open('Zadacha1HW.txt', 'w')
# data.writelines(Fibbonacci())
data.close()


# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.


def Fruits():
    file = open("fruits.txt", encoding='utf-8')
    fruitsnames = file.readlines()
    file.close()
    print(fruitsnames)

    letter = input("Первая буква для поиска: ")

    for i in fruitsnames:
        if i[0].lower() == letter.lower():
            print(i)
# Fruits()


# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

# «как тебя зовут?» –> меня зовут Анатолий




# Не уверен что сделал так, как нужно, но время сильно поджимало для чего-то более масштабного


user_phrase = input('Введите текст: ')

phrases = {'привет':'Здравствуйте', 'как тебя зовут':'Анатолий', 'сколько тебе лет':'Я появился недавно'}

if user_phrase.lower() in phrases:
        print(phrases.get(user_phrase))
else:
    print('Я тебя не понимаю, давай заново')

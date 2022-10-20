
            # ЗАДАЧА 0

def ReadLastRow():
    data = open('text.txt', encoding='utf-8')
    print(data)
    text = data.readlines()
    print(text[-1])
    data.close()


            

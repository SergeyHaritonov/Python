# Задача 4*. Создайте игру в крестики-нолики.


maps = [1,2,3,
        4,5,6,
        7,8,9]
 

win_lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
 
def print_maps():
    print(maps[0], end = " | ")
    print(maps[1], end = " | ")
    print(maps[2])
    print('==========') 
    print(maps[3], end = " | ")
    print(maps[4], end = " | ")
    print(maps[5])
    print('==========')
    print(maps[6], end = " | ")
    print(maps[7], end = " | ")
    print(maps[8])    
 
def who_win():
    win = ""
    for i in win_lines:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Победил игрок 1 (Х)!"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Победил игрок 2 (O)!"        
    return win
 
i=1

print_maps()
while i<10:
    if i%2!=0:
        step =int(input("ход игрока 1: "))
        if step>9 or step<1:
            print("Номера ячеек лежат в диапазоне от 1 до 9. Начните игру сначала")
            break
        if maps[step-1]!="X"and maps[step-1]!="O":
            maps[step-1]="X"
        else:
            print("Эта ячейка уже занята,  начните игру сначала")
            break
    else:
        step =int(input("ход игрока 2: "))
        if maps[step-1]!="X"and maps[step-1]!="O":
            maps[step-1]="O"
        else:
            print("Эта ячейка уже занята начните игру сначала")
            break
        
    print_maps()
    win= who_win()
    if win!='':
        print(win)
        break
    i+=1
    
if win=='':
    print("Ничья!")

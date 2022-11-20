
import model

def createMenu():
    print('1 - дней до нового года')
    print('введите нужный пункт меню: ')
    print('1')
    printResult()

def printResult():
    print(f'{model.newYear()} дней до нового года')

import datetime as dt

def newYear():
    current_date = dt.datetime.now()
    new_year = dt.datetime(current_date.year + 1, 1, 1)
    # print(new_year - current_date) # Результат -> 46 days, 13:23:22.824414
    # print(f'{(new_year - current_date).days} дней до нового года') # Разница между датами это тоже дата, поэтому поставив после нее точку можно также работать со свойствами.
                                      # Например, свойство days округляет разницу до дней, отбрасывая часы, минуты и т.д.
    return (new_year - current_date).days # Здесь print не нужен, т.к. здесь работаем только с данными. Здесь нужен return,
                                          # а вся визуализация будет во view.
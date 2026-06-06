from datetime import datetime

def get_days_from_today(target_date : str):

    current_date = datetime.now()                               # зберігаєму сьогоднішу дату в об'єкті datetime 
    current_date_in_days = current_date.toordinal()             # переводимо в ordinal для математичних маніпуляцій
    
    possible_formats = ["%Y.%m.%d", "%Y-%m-%d", "%Y/%m/%d"]     # можливі формати для запису дати (можно додавати можливі варіанти)

    for i in possible_formats:                                  # цикл for для спроб для переносення str до datetime
        try:
            datetime_objekt = datetime.strptime(target_date, i)    # спроба перенести і в цій строці це можливий формат
        except ValueError:
            pass
    datetime_objekt_in_days = datetime_objekt.toordinal()       # переводимо в ordinal для математичних маніпуляцій

    delta = current_date_in_days - datetime_objekt_in_days      # вираховуєму різницю днів між датами

    return delta

print(get_days_from_today("2025-06-06"))                        # Вивід: 365

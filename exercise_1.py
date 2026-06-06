from datetime import datetime

def get_days_from_today(date : str):
    current_date = datetime.now()
    target_date = date
    current_date_days = current_date.toordinal()
    target_date_days = target_date.toordinal()
    delta_days = current_date_days - target_date_days
    return delta_days

def get_info():

    years_set_right = False #змінні для трекінгу встановлення правильних значень

    month_set_right = False #змінні для трекінгу встановлення правильних значень

    days_set_right = False  #змінні для трекінгу встановлення правильних значень

    print("Hi, what is your date?")

    while years_set_right == False:               # користувач вписуює значення доки воно не буде число, яке підходить для року (не меньше 0)
        try:
            years = int(input("Years? "))

            if years < 0:
                print("Wrong value. Try again")
            else:
                years_set_right = True
        except ValueError:
            print("Sorry, did not work")    

    while month_set_right == False:               # користувач вписуює значення доки воно не буде число, яке підходить для місяцю
        try:                                      
            months = int(input("Month? "))

            if months < 0 or months > 12:         # не меньше 0 та не більше 12
                print("Wrong value. Try again")
            else:
                month_set_right = True
        except ValueError:
            print("Sorry, did not work") 


    while days_set_right == False:                 # користувач вписуює значення доки воно не буде число, яке підходить для дню
        try:
            days = int(input("Day? "))

            if days < 1 or days > 31:              # не меньше 1 та не більше 31
                print("Wrong value. Try again")
            elif months in (4, 6, 9 , 11) and days > 30:        # якщо місяц має тільки 30 днів, то число днів має бути меньшим за 31
                print("Sorry, wrong number. Try again")
            elif months == 2 and days > 29:                     # якщо місяц лютий, то число днів має бути меньшим за 29
                print("Sorry, wrong number. Try again")         # міг би імплемінтувати перевірку високісного року, але подібна
            else:                                               # потрібна функція знаходиться в іншій біліотеці (calendar)
                days_set_right = True
        except ValueError:
            print("Sorry, did not work") 

    date = datetime(year=years, month=months, day=days)         # усі значення зберігаю в об*єкт datetimе т.я. в завданні в функцію
    return date                                                 # get_days_from_today повинен бути передан аргумент типу datetime

target_date = get_info()
delta = get_days_from_today(target_date)

print(delta, " days")
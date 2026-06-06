import random


def get_numbers_ticket(min, max, quantity):
    list_of_numbers = []                            # список для зберігання випадкових чисел
    for i in range(quantity):                       
        randint = random.randint(min, max)          # створювання випадкового числа між min та max 
        if randint not in list_of_numbers:
            list_of_numbers.append(random.randint(min,max)) # додавання числа до списку, якщо його там ще немає
        else:
            i = i - 1                               # якщо число є, то відкатуємо ітерацію, щоб в кінці мали достатню кількість чисел
    list_of_numbers.sort()                          # сортування списку 
    return list_of_numbers



def get_numbers():

    result = []                                     # список для зберігання результату
    min_set = False
    max_set = False
    quantity_set = False

    while min_set == False:                         # цикл буде працювати доки користувач не впише правільне число
        try:
            min = int(input("What is the minumum? "))
            if min > 0 and min < 1000:              # min має бути більше за 0 та меньше за 1000
                min_set = True
                result.append(min)                  # додаємо до списку результатів
            else:
                print("Sorry, wrong value. Try again")
        except ValueError:
            print("Sorry, wrong value. Try again ")

    while max_set == False:                         # цикл буде працювати доки користувач не впише правільне число
        try:
            max = int(input("What is the maximum? "))
            if max <= 1000 and max > min:           # max має бути більше за min та меньше за 1000
                max_set = True
                result.append(max)                  # додаємо до списку результатів
            else:
                print("Sorry, wrong value. Try again")
        except ValueError:
            print("Sorry, wrong value. Try again ")

    while quantity_set == False:                    # цикл буде працювати доки користувач не впише правільне число
        try:
            quantity = int(input("What is the quantity? "))
            if quantity < max and quantity <= (max - min) and quantity > 0:             # quantity має бути меньше max, більше за 0, та бути меньшим або рівним за кілкість усіх числе між min та max
                quantity_set = True
                result.append(quantity)
            else:
               print("Sorry, wrong value. Try again")
        except ValueError:
            print("Sorry, wrong value. Try again ")
    return result
    

user_answers = get_numbers()

user_answer_min = user_answers[0]
user_answer_max = user_answers[1]
user_answer_quantity = user_answers[2]

print(get_numbers_ticket(user_answer_min, user_answer_max, user_answer_quantity))



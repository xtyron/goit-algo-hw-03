import random

def get_numbers_ticket(min, max, quantity):

    list_of_numbers = []                                # список для зберігання випадкових чисел

    if min > 0 and min < 1000 and max <= 1000 and max > min and quantity < (max - min):    

        while len(list_of_numbers) != quantity:                       
            randint = random.randint(min, max)          # створювання випадкового числа між min та max 
            if randint not in list_of_numbers:
                list_of_numbers.append(randint)         # додавання числа до списку, якщо його там ще немає
        list_of_numbers.sort()                          # сортування списку 
    else:
        print("Sorry, wrong values")
    return list_of_numbers


print(get_numbers_ticket(1, 10, 5))                         
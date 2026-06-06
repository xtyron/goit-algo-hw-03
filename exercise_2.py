import random


def get_numbers_ticket(min, max, quantity):
    list_of_numbers = []
    for i in range(quantity):
        randint = random.randint(min, max)
        if randint not in list_of_numbers:
            list_of_numbers.append(random.randint(min,max))
        else:
            i = i - 1
    list_of_numbers.sort()
    return list_of_numbers



def get_numbers():

    result = []
    min_set = False
    max_set = False
    quantity_set = False

    while min_set == False:
        try:
            min = int(input("What is the minumum? "))
            if min > 0 and min < 1000:
                min_set = True
                result.append(min)
            else:
                print("Sorry, wrong value. Try again")
        except ValueError:
            print("Sorry, wrong value. Try again ")

    while max_set == False:
        try:
            max = int(input("What is the maximum? "))
            if max <= 1000 and max > min:
                max_set = True
                result.append(max)
            else:
                print("Sorry, wrong value. Try again")
        except ValueError:
            print("Sorry, wrong value. Try again ")

    while quantity_set == False:
        try:
            quantity = int(input("What is the quantity? "))
            if quantity < max and quantity <= (max - min) and quantity > 0:
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



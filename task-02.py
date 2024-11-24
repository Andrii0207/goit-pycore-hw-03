import random


def get_numbers_ticket(min, max, quantity):
    k = 0
    result = []
    while k < quantity:
        if min < 1 or max > 1000:
            print ("array must be in range from 1 to 1000")
            break

        random_number = random.randint(min, max)
        result.append(random_number)
        k += 1
    result.sort()
    return result
   



lottery_numbers =  get_numbers_ticket(1, 1000, 5)
print("Ваші лотерейні числа:", lottery_numbers)
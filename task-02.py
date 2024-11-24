import random


def get_numbers_ticket(min, max, quantity):
    k = 0
    result = []
    while k < quantity:
        random_number = random.randint(min, max)
        result.append(random_number)
        k += 1
    result.sort()
    return result



print(get_numbers_ticket(1, 100, 5))

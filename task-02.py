import random


def get_numbers_ticket(min, max, quantity):
    k = 0
    result = []

    while k < quantity:
    
        if (max - min) < quantity:
            print("You should increase number range or decrease quantity of number")
            break
    
        if min < 1 or max > 1000:
            print ("Enter numbers must be in range from 1 to 1000")
            break
     
        random_number = random.randint(min, max)

        if random_number in result:
            continue
        
        result.append(random_number)
        k += 1
        result.sort()
    return result
   

lottery_numbers =  get_numbers_ticket(2, 8, 5)
print("Ваші лотерейні числа:", lottery_numbers)
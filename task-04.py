from datetime import datetime
from datetime import timedelta

users = [
    {"name": "John Doe", "birthday": "1985.11.04"}, # 0 Monday birthday left
    {"name": "Jane Smith", "birthday": "1990.11.27"}, # 2 Wednesday current week
    {"name": "Sarah Smile", "birthday": "1990.11.30"}, # 5 Saterday birthday this week / congratulation next week
    {"name": "Bob Marley", "birthday": "1990.12.01"}   # 1 Thuesday birthday this week / congratulation next week
]

def get_upcoming_birthdays(users):

    congratulation_list = []

    today = datetime.today().date()

    for user in users:
        birthday = user["birthday"]
        birthday_this_year_string = birthday.replace(birthday[:4], str(today.year))
        birthday_this_year = datetime.strptime(birthday_this_year_string, "%Y.%m.%d").date()
      
        if birthday_this_year < today:
            birthday_next_year = birthday_this_year.replace(year=today.year + 1)
            print("Your birthday next year", birthday_next_year)
   
        else:
            difference_days = birthday_this_year - today
                 
            if difference_days.days < 7 and birthday_this_year.weekday() in (5, 6):
                congratulation_date = birthday_this_year + timedelta(days=(7 - difference_days.days))
                congratulation_list.append({"name": user["name"], 'congratulation_date': congratulation_date.strftime("%Y.%m.%d")})
            else:
                print("Your birthday is comming soon >>>", birthday_this_year)
    return congratulation_list

       
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

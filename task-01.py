from datetime import datetime

def get_days_from_today(date):
    formatted_date = datetime.strptime(date, "%Y-%m-%d")
    now = datetime.today()
    delta = now - formatted_date
    return print(delta.days)
    

get_days_from_today("2021-10-09")

from datetime import datetime


def get_days_from_today(date):

    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")
        now = datetime.today()
        delta = now - formatted_date

    except ValueError:
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")

    return print(delta.days)

get_days_from_today("2020-10-09")

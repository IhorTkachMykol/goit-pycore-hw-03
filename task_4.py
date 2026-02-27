from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Повертає список колег, яких потрібно привітати протягом наступних 7 днів.
    Якщо день народження припадає на вихідний — переносить на понеділок.
    """

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо дату народження у datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця у днях між сьогодні і ДН
        days_diff = (birthday_this_year - today).days

        # Перевіряємо, чи ДН у межах наступних 7 днів
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            # Переносимо привітання, якщо вихідний
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            # Формуємо результат
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
users = [
    {"name": "Ivan Popenko", "birthday": "1985.02.12"},
    {"name": "Mykola Hmil", "birthday": "1990.02.09"},
    {"name": "Olexa Melnyk", "birthday": "1992.02.14"},
]

upcoming = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming)

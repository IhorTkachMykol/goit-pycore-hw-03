from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворюємо введений рядок у дату
        user_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")

    # Перетворення дат у кількість днів
    today = datetime.today().date()
    difference = today - user_date

    return difference.days


# --- Основна частина ---
user_date = input("Введіть дату у форматі YYYY-MM-DD: ")

try:
    result = get_days_from_today(user_date)
    print("Кількість днів між заданою датою і сьогоднішньою:", result)
except ValueError as e:
    print(e)

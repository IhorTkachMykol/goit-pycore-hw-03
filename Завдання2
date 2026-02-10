import random

def get_numbers_ticket(min_value, max_value, quantity):
    # Перевірка валідності параметрів
    if (
        not isinstance(min_value, int)
        or not isinstance(max_value, int)
        or not isinstance(quantity, int)
        or min_value < 1
        or max_value > 1000
        or min_value > max_value
        or quantity <= 0
        or quantity > (max_value - min_value + 1)
    ):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)


# --- Основна частина програми ---

try:
    user_min = int(input("Введіть мінімальне число (min): "))
    user_max = int(input("Введіть максимальне число (max): "))
    user_quantity = int(input("Скільки чисел потрібно вибрати (quantity): "))

    result = get_numbers_ticket(user_min, user_max, user_quantity)

    if result:
        print("Ваші лотерейні числа:", result)
    else:
        print("Помилка: некоректні параметри. Спробуйте ще раз.")

except ValueError:
    print("Помилка: потрібно вводити тільки цілі числа.")

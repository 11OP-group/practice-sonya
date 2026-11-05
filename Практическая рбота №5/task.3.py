# Задача 3. Конвертер валют

# курс доллара
USD_TO_RUB = 95.50


def convert_usd_to_rub(amount_usd):
    """Переводит сумму из долларов в рубли."""
    amount_rub = amount_usd * USD_TO_RUB
    return amount_rub


# ввод суммы в долларах
dollars = float(input("Введите сумму в долларах: "))

# вызов функции
rubles = convert_usd_to_rub(dollars)

# вывод результата
print(f"Сумма в долларах: {dollars:.2f} USD")
print(f"Сумма в рублях: {rubles:.2f} руб.")

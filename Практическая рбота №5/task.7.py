# Задача 7. Рефакторинг калькулятора поездки на такси

# константа: цена бензина за литр
FUEL_PRICE = 49.5
def calculate_trip_cost(distance_km, fuel_consumption_per_100km):
    """
    Рассчитываем расход топлива и стоимость поездки на такси

    Args:
        distance_km (float): расстояние поездки в километрах
        fuel_consumption_per_100km (float): расход топлива машины на 100 км в литрах

    Returns:
        tuple: (расход топлива в литрах, стоимость поездки в рублях)
    """
    total_liters = distance_km * (fuel_consumption_per_100km / 100)
    total_price = total_liters * FUEL_PRICE_PER_LITER
    return total_liters, total_price


# вводим цифры
distance_km = float(input("Какое расстояние (км)? "))
fuel_consumption_per_100km = float(input("Сколько литров на 100 км ест машина? "))

total_liters, total_price = calculate_trip_cost(distance_km, fuel_consumption_per_100km)

# вывод
print(f"Нужно бензина: {total_liters:.2f} л")
print(f"Стоимость поездки: {total_price:.2f} руб")


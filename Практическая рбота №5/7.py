FUEL_PRICE_PER_LITER = 49.5
CONSUMPTION_BASE_KM = 100

def calculate_fuel_amount(distance_km, consumption_per_100km):
    """
    Считает, сколько бензина нужно на поездку
    и возвращает количество бензина в литрах
    """
    return distance_km * consumption_per_100km / CONSUMPTION_BASE_KM

def calculate_fuel_cost(fuel_liters, price_per_liter):
    """
    Считает стоимость бензина
    и возвращает стоимость в рублях
    """
    return fuel_liters * price_per_liter

def calculate_trip_cost():
    """Запрашивает данные, вызывает расчёты и выводит результат"""
    print("Калькулятор стоимости бензина для поездки")

    distance_km = float(input("Введите расстояние поездки км: "))
    consumption_per_100km = float(input("Введите расход автомобиля на 100км: "))

    fuel_liters = calculate_fuel_amount(distance_km, consumption_per_100km)
    fuel_cost = calculate_fuel_cost(fuel_liters, FUEL_PRICE_PER_LITER)

    print(f"Потребуется бензина: {fuel_liters:.2f} л")
    print(f"Стоимость бензина: {fuel_cost:.2f} руб")

calculate_trip_cost()
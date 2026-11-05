# Задача 4. Калькулятор площади

PI = 3.1415


def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника

    Args:
        width (float): ширина.
        height (float): высота.

    Returns:
        float: площадь прямоугольника
    """
    return width * height


def calculate_circle_area(radius):
    """
    Вычисляет площадь круга

    Args:
        radius (float): радиус круга.

    Returns:
        float: площадь круга
    """
    return PI * radius * radius


# вводим и считаем прямоугольность
width, height = map(float, input("Введите ширину и высоту прямоугольника: ").split())
rectangle_area = calculate_rectangle_area(width, height)

# выводим прямоугольность
print(f"Площадь прямоугольника равна {rectangle_area:.2f}")

# вводим и считаем кругность
radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(radius)

# выводим кругность
print(f"Площадь круга равна {circle_area:.2f}")
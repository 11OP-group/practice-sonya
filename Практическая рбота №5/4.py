from math import pi

def calculate_rectangle_area(width, height):
    """
    принимает ширину и высоту
    и возвращает площадь прямоугольника
    """
    area_rectangle = width * height
    return area_rectangle

def calculate_circle_area(radius):
    """
    принимает радиус круга
    и возвращает площадь круга

    """
    circle_area = pi * radius * radius
    return circle_area

width, height = map(float, input("Введите стороны прямоугольника: ").split())
area_rectangle = calculate_rectangle_area(width, height)

print(f"Площадь прямоугольника равна {area_rectangle:.2f}")

radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(radius)

print(f"Площадь круга равна {circle_area:.2f}")
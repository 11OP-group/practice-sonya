# Задача 2. Цвета колеса рулетки
MIN_POCKET = 0
MAX_POCKET = 36

pocket = int(input("Введите номер вашего кармана: "))

if pocket < MIN_POCKET or pocket > MAX_POCKET:
    print("Данные неверны")
elif pocket == 0:
    print("Ваш карман зеленый")
elif 1 <= pocket <= 10 or 19 <= pocket <= 28:
    if pocket % 2 == 1:
        print("Ваш карман красный")
    else:
        print("Ваш карман черный")
else:
    if pocket % 2 == 1:
        print("Ваш карман черный")
    else:
        print("Ваш карман красный")
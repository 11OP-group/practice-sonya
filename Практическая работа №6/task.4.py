# Задача 4. Ход слона
MIN_SQUARE = 1
MAX_SQUARE = 8

column1, row1 = map(int, input(f"Введите столбец и строку клетки со слоном ({MIN_SQUARE}-{MAX_SQUARE}) через пробел: ").split())
column2, row2 = map(int, input(f"Введите столбец и строку клетки для хода ({MIN_SQUARE}-{MAX_SQUARE}) через пробел: ").split())

if (not MIN_SQUARE <= column1 <= MAX_SQUARE or not MIN_SQUARE <= row1 <= MAX_SQUARE
        or not MIN_SQUARE <= column2 <= MAX_SQUARE or not MIN_SQUARE <= row2 <= MAX_SQUARE):
    print("Данные неверны!")
elif column1 == column2 and row1 == row2:
    print("Данные неверны!")
elif abs(column1 - column2) == abs(row1 - row2):
    print("Слон может сделать этот ход!")
else:
    print("Слон не может сделать этот ход!")
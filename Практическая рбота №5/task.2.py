# Задача 2. Калькулятор ИМТ
# вводим вес и рост
weight, height = map(float, input("Введите вес (кг) и рост (м): ").split())

# считаем ИМТ
bmi = weight / (height * height)

# вывод
print(f"Ваш ИМТ равен {bmi:.1f}")

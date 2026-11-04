weight, height = map(float, input("Введите свой вес и рост в метрах: ").split())

bmi = weight / height **2

print(f"Индекс массы тела равен: {bmi:.1f}")
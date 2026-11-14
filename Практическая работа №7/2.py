
import random

status = input("введите статус заказа:").lower()

# input() — пользователь вводит статус заказа
# .lower() — делает все буквы маленькими. Например, SHIPPED в shipped

match status:  # начинает проверять статус
    case "pending":
        # если заказ ожидает обработки, выводится соответствующая информация
        print(f"статус:в ожидании ⏳")
        print(f"описание: заказ ожидает обработки.")
        print(f"время ожидания: {random.randint(2, 5)} дня")

    case "processing":
        print(f"статус:в обработке ⚙️")
        print(f"описание: заказ собирается.")
        print(f"время ожидания: {random.randint(3, 6)} дня")

    case "shipped":
        print(f"статус:отправлено 🚚")
        print(f"описание:заказ находится в пути.")
        print(f"время ожидания: {random.randint(4, 8)} дней")

    case "delivered":
        print(f"статус:доставлено 📦")
        print(f"описание:заказ уже доставлен.")
        print(f"время ожидания: 0 дней")

    case "cancelled":
        print(f"статус:отменено ❌")
        print(f"описание:заказ был отменён.")
        print(f"время ожидания:не требуется")

    case _:
        print(f"ошибка! неизвестный статус заказа.")
        print(f"доступные статусы: pending, processing, shipped, delivered, cancelled")

def vydat_kupyury(ostatok, kupyura):
    """
    Считает сколько купюр каждого номинала можно выдать,
    Печатает количество купюр и возвращает остаток
    """
        
    kolichestvo = ostatok // kupyura
    print(f"Купюр по {kupyura}: {kolichestvo}")
    return ostatok % kupyura

summa = int(input("Введите сумму для снятия: "))
ostatok = summa

print(f"Выдача суммы {summa} руб:")

ostatok = vydat_kupyury(ostatok, 5000)
ostatok = vydat_kupyury(ostatok, 2000)
ostatok = vydat_kupyury(ostatok, 1000)
ostatok = vydat_kupyury(ostatok, 500)
ostatok = vydat_kupyury(ostatok, 200)
ostatok = vydat_kupyury(ostatok, 100)

print(f"Остаток: {ostatok} руб")
fist = int(input("Введите первое число"))
 while True:
     second = int(input("Введите второе число"))
     if second > first:
         break
     else:
     print("Ошибка!Введите число заново")
     while True:
         third = int(input("Введите третье число"))
         if third > second:
             break
         else:
         print ("Ошибка!Введите число заново")
         print("Последовательность принята")
def ask_for_int():
    while True:
        try:
            result = int(input("Пожалуйста, введите число"))
        except:
            print("Вы ввели не число")
            continue
        else:
            print("Спасибо, что ввели число")
            break


ask_for_int()

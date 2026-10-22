def convert():
    choice = input("Выберите направление (1 — кг в г, 2 — г в кг): ")

    if choice not in ['1', '2']:
        print("Ошибка: неверный выбор направления.")
        return

    try:
        val = float(input("Введите числовое значение: "))
    except ValueError:
        print("Ошибка: введено не число! Пожалуйста, используйте цифры.")
        return

    if choice == '1':
        result = val * 1000
        print(f"Результат: {val} кг = {result} г")
    else:
        result = val / 1000
        print(f"Результат: {val} г = {result} кг")

convert()
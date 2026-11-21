numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
if not numbers:
    print("Список порожній")
else:
    minimum = maximum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n

    difference = maximum - minimum
    print(f"Мінімум: {minimum}, Максимум: {maximum}, Різниця: {difference}")
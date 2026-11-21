arr = list(map(int, input("Введіть числа через пробіл: ").split()))
if not arr:
    print("Список порожній")
else:
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    print(f"Максимальна сума підмасиву {arr[start:end + 1]}: {max_sum}")
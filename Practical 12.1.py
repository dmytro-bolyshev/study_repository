def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

data = list(map(int, input("Введіть числа через пробіл: ").split()))
print(f"Відсортований масив: {bubble_sort(data)}")
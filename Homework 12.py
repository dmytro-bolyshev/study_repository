def counting_sort(arr):
    if not arr:
        return []
    k = max(arr)
    counts = [0] * (k + 1)
    for x in arr:
        counts[x] += 1
    result = []
    for value in range(k + 1):
        result.extend([value] * counts[value])
    return result


data = list(map(int, input("Введіть числа через пробіл: ").split()))
print(f"Відсортований масив: {counting_sort(data)}")
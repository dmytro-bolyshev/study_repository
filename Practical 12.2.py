def counting_sort(arr):
    if not arr:
        return []
    k = max(arr)
    counts = [0] * (k + 1)
    for x in arr:
        counts[x] += 1
    for i in range(1, k + 1):
        counts[i] += counts[i - 1]
    result = [0] * len(arr)
    for x in reversed(arr):
        counts[x] -= 1
        result[counts[x]] = x
    return result

data = list(map(int, input("Введіть числа через пробіл: ").split()))
print(f"Відсортований масив: {counting_sort(data)}")
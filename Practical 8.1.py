prices = [152, 124, 76, 237, 274, 310, 315, 302, 240, 272, 201, 190]
s = sum(prices[:3])
best = s
best_start = 0

for i in range(3, len(prices)):
    s += prices[i] - prices[i - 3]
    if s > best:
        best = s
        best_start = i - 3 + 1
print(f"Максимальна ціна вікна за три дні: {best}")
print(f"Дні вікна: {list(range(best_start, best_start + 3))}")
print(f"Ціна за акції поденно: {prices[best_start:best_start + 3]}")
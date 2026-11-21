n = int(input("Введіть N: "))
primes = []
total = 0
for num in range(2, n + 1):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
        total += num

if primes:
    expression = "+".join(map(str, primes))
    print(f"Сума простих чисел від 2 до {n} ({expression}): {total}")
else:
    print(f"У діапазоні від 2 до {n} простих чисел немає")
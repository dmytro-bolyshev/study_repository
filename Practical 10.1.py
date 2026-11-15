def fast_exp(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / fast_exp(x, -n)
    half = fast_exp(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x

print(fast_exp(2, 10))
print(fast_exp(3, 5))
print(fast_exp(2, -3))
def intersect_slow(a, b):
    result = []
    steps = 0
    for x in a:
        for y in b:
            steps += 1
            if x == y:
                result.append(x)
                break
    return result, steps

def intersect_fast(a, b):
    seen = set(a)
    steps = len(a)
    result = []
    for y in b:
        steps += 1
        if y in seen:
            result.append(y)
    return result, steps

print(intersect_slow([1, 2, 3, 4], [3, 4, 5]))
print(intersect_fast([1, 2, 3, 4], [3, 4, 5]))

for n in (100, 500, 1000, 2000):
    a = list(range(n))
    b = list(range(n, 2 * n))
    _, slow = intersect_slow(a, b)
    _, fast = intersect_fast(a, b)
    print(f"N = M = {n:>5} | повільний: {slow:>9} кроків | швидкий: {fast:>5} кроків")
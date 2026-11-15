def list_search(data, target):
    steps = 0
    for x in data:
        steps += 1
        if x == target:
            break
    return steps

def build_table(data, size):
    table = [[] for _ in range(size)]
    for x in data:
        table[x % size].append(x)
    return table

def set_search(table, target):
    steps = 1
    for x in table[target % len(table)]:
        steps += 1
        if x == target:
            break
    return steps

for n in (1_000, 10_000, 100_000, 1_000_000):
    data = list(range(n))
    table = build_table(data, n)
    target = n - 1

    print(f"N = {n:>9} | list: {list_search(data, target):>9} шагів | set: {set_search(table, target)} шага")
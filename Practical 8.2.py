consumption = [3, 2, 2, 4, 6, 9, 12, 8, 5, 4, 3, 3]
limit = 15
p = [0]
for x in consumption:
    p.append(p[-1] + x)
queries = [(0, 2), (3, 5), (6, 8), (9, 11)]
for l, r in queries:
    t = p[r + 1] - p[l]
    status = "ПЕРЕВИЩЕННЯ" if t > limit else "норма"
    print(f"години {l}-{r}: {t} кВт·год, {status}")
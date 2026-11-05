while True:
    n = int(input("Введіть число: "))
    fibb = [n, n]
    while len(fibb)<10:
        fibb.append(fibb[-1]+fibb[-2])
    print(fibb)
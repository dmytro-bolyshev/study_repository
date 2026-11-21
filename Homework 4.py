number = int(input("Введіть число: "))
mask = 1 << 3
bit_is_on = (number & mask) != 0
result = number << 3
print(f"3-й біт увімкнений: {bit_is_on}, Число * 8: {result}")
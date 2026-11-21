def digital_root(n):
    n = abs(n)
    if n < 10:
        return n
    digit_sum = sum(int(d) for d in str(n))
    return digital_root(digit_sum)

number = int(input("Введіть число: "))
print(f"Цифровий корінь: {digital_root(number)}")
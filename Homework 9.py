def calculate_discount(price, discount_percent):
    if not price >= 0:
        raise ValueError("Ціна не може бути від'ємною")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Відсоток знижки має бути в межах від 0 до 100")
    return price * (100 - discount_percent) / 100

def raises_value_error(*args):
    try:
        calculate_discount(*args)
    except ValueError:
        return True
    return False

assert calculate_discount(200.0, 15.0) == 170.0
assert calculate_discount(100, 0) == 100       # без знижки
assert calculate_discount(100, 100) == 0       # знижка 100 %
assert calculate_discount(0, 50) == 0          # нульова ціна
assert calculate_discount(50, 50) == 25.0
assert round(calculate_discount(19.99, 10), 2) == 17.99

assert raises_value_error(-1, 10)              # від'ємна ціна
assert raises_value_error(100, -5)             # відсоток менший за 0
assert raises_value_error(100, 100.1)          # відсоток більший за 100
assert raises_value_error(100, 101)
assert raises_value_error(float("nan"), 10)    # NaN у ціні
assert raises_value_error(100, float("nan"))   # NaN у відсотку

print(calculate_discount(200.0, 15.0))
print("Автотести пройшли успішно")
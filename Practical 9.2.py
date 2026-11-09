RATES = {"USD": 1.0, "EUR": 0.92, "UAH": 41.5}
def require(condition, message):
    if not condition:
        raise ValueError(f"Помилка: {message}")

def convert(amount, conv_input, conv_output):
    require(isinstance(amount, (int, float)), "Повинен бути числом")
    require(amount >= 0, "Повинен бути більше нуля!")
    require(conv_input in RATES, f"Невідома валюта! {conv_input}")
    require(conv_output in RATES, f"Невідома валюта! {conv_output}")
    require (amount is not int or float, f"Не є числом!")

    return round(amount / RATES[conv_input] * RATES[conv_output], 2)

conv_input = input("Введіть валюту з якої хочете перевести:\nUAH\nUSD\nEUR\n: ")
conv_output = input("Введіть валюту у яку хочете перевести:\nUAH\nUSD\nEUR\n: ")
count = input("Введіть суму: ")
count = int(count)

print(f"{convert(count, conv_input, conv_output)}")